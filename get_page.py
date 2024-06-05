import color

#parsing
def get_page(soup):
    board = soup.find("div", class_="board")
    threads = board.find_all("div", class_="thread")

    #for each thread
    for thread in threads:
        postContainer = thread.find("div", class_="postContainer opContainer")
        postOp = postContainer.find("div", class_="post op")
        postInfoDesk = postOp.find("div", class_="postInfo desktop")

        subject = postInfoDesk.find("span", class_="subject")

        #check if there is a title
        if len(subject) > 0:
            print(color.colors.BLUE + subject.text.strip() + color.colors.END)
        else:
            print(color.colors.BLUE + "**no title**" + color.colors.END)
