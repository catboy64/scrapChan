import color, os


#parsing
def get_page(soup):
    i = 0
    board = soup.find("div", class_="board")
    threads = board.find_all("div", class_="thread")

    #for each thread
    for thread in threads:
        i = i + 1
        os.system("clear")
        postContainer = thread.find("div", class_="postContainer opContainer")
        postOp = postContainer.find("div", class_="post op")
        blockquote = postOp.find("blockquote", class_="postMessage")
        postInfoDesk = postOp.find("div", class_="postInfo desktop")
        subject = postInfoDesk.find("span", class_="subject")

        postContainerReplys = thread.find_all("div", class_="postContainer replyContainer")


        #check if there is a title
        if len(subject) > 0:
            print(color.colors.BLUE + subject.text.strip() + color.colors.END)
        else:
            print(color.colors.BLUE + "**no title**" + color.colors.END)

        print(blockquote.text.strip())
        print()
        print()

        for reply in postContainerReplys:
            print(color.colors.GREEN + "Anon" + color.colors.END)
            postReply = reply.find("div", class_="post reply")
            replyMessage = postReply.find("blockquote", class_="postMessage")
            print(replyMessage.text)
            print()

        print(str(i) + "/15")
        input()
