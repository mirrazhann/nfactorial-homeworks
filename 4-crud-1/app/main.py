from fastapi import FastAPI, Request, Response, Form, Query, HTTPException, Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from repository.book import BookRepository

app = FastAPI()
repository = BookRepository()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
    
@app.get("/books", response_model=list[dict])
def get_books(
    request: Request,
    page: int = Query(1, ge=1, description="Номер страницы"),
    limit: int = Query(10, ge=1, le=50, description="Кол-во книг на странице")
):
    start = (page - 1) * limit
    end = start + limit
    book_count = repository.get_len()
    total_pages = -(-book_count // limit)  # Округление вверх
    books = repository.get_all(start, end)
    prev = None if page <= 1 or page > total_pages else page-1
    next = None if page >= total_pages or page < 1 else page+1
    return templates.TemplateResponse("books/list.html", {"request":request, "books": books, "prev": prev, "next":next})

@app.get("/books/new")
def add_book(request: Request):
    return templates.TemplateResponse("books/new.html", {"request": request})

@app.post("/books/new")
def add_book(
    request: Request, 
    title: str = Form(), 
    author: str = Form(),
    year: int = Form(),
    total_pages: int = Form(),
    genre: str = Form()
):
    datas = {
        "request": request, 
        "title": title,
        "author": author,
        "year": year,
        "total_pages": total_pages,
        "genre": genre
    }
    if title == "":
        datas["error"] = "Заполните название!"
        return templates.TemplateResponse("books/new.html", datas)
    elif author == "":
        datas["error"] = "Не указан автор!"
        return templates.TemplateResponse("books/new.html", datas)
    elif total_pages <= 0:
        datas["error"] = "Не корректное число страниц!"
        return templates.TemplateResponse("books/new.html", datas)
    elif genre == "":
        datas["error"] = "Не указан жанр!"
        return templates.TemplateResponse("books/new.html", datas)
    repository.save(datas)
    # получить последнюю страницу и добавить в ссылку
    book_count = repository.get_len()
    total_book_pages = -(-book_count // 10)  # Округление вверх
    return RedirectResponse(url=f"/books?page={total_book_pages}", status_code=303)

@app.get("/books/{id}")
def get_book(request: Request, id: int = Path(..., title="Book ID")):
    book = repository.get_one(id)
    if not book:
        raise HTTPException(status_code=404, detail="Not Found")
    return templates.TemplateResponse("books/detail.html", {"request":request, "book": book})

