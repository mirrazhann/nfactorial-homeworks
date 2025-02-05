class VoxPop:
    def __init__(self, comments_count=5):
        self.comments = []
        self.comments_count = comments_count

    def add_comment(self, text, category):
        if category.lower() not in ["+", "-"]:
            print("Error! Incorrect category type")
            return
        self.comments.insert(0, {"text": text, "category": category})
        print("Comment added")

    def show_comments(self, page=1):
        if not self.comments:
            print("No comments")
            return
        
        start = (page - 1) * self.comments_count
        end = start + self.comments_count
        
        for idx, comment in enumerate(self.comments[start:end], start=start + 1):
            print(f"{idx}. [{comment['category']}] {comment['text']}")
        
        print(f"\nPage {page} из {((len(self.comments) - 1) // self.comments_count) + 1}\n")

if __name__ == "__main__":
    voxpop = VoxPop()
    while True:
        action = input("Choose action: (1) Add comment, (2) Show Comments, (3) Exit: ")
        if action == "1":
            text = input("Your comment: ")
            category = input("Category positive (+) or negative (-): ")
            voxpop.add_comment(text, category)
        elif action == "2":
            page = int(input("Inter page number: ") or 1)
            voxpop.show_comments(page)
        elif action == "3":
            print("Exit")
            break
        else:
            print("Error action! Choose again!")
