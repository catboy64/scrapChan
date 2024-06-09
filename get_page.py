import color, os, requests
from bs4 import BeautifulSoup
from ascii_magic import AsciiArt

#parsing
def get_page(soup, URL):
    ogURL = URL
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
        
        #no
        postNumDesk = postInfoDesk.find("span", class_="postNum desktop")
        no = postNumDesk.find_all("a")
        
        #check if there is a title
        if len(subject) > 0:
            print(color.colors.BLUE + subject.text.strip() + color.colors.END + " No." + no[1].text + "\n")
        else:
            print(color.colors.BLUE + "**no title**" + color.colors.END + " No." + no[1].text + "\n")
        
        #image
        file = postOp.find("div", class_="file")
        fileThumb = file.find("a", class_="fileThumb")
        if fileThumb:
            img = fileThumb.find("img")
            imgURL = img['src']
            imgURL = "https:"+imgURL
            img_data = requests.get(imgURL).content
            with open("Pic/picture"+str(i)+".jpg", 'wb') as handler:
                handler.write(img_data)
            imgMagic = AsciiArt.from_image("Pic/picture"+str(i)+".jpg")
            imgMagic.to_terminal(columns=40)
            print()

        postContainerReplys = thread.find_all("div", class_="postContainer replyContainer")

        blockquote = str(blockquote).replace("</br>", "\n")
        blockquote = str(blockquote).replace("<br/>", "\n")
        blockquote = BeautifulSoup(blockquote, "html.parser")
        print(blockquote.text.strip())
        print()
        print()
        
        #recent replys (not sure if I want them or not)
        #for reply in postContainerReplys:
        #    
        #    postReply = reply.find("div", class_="post reply")
        #    replyMessage = postReply.find("blockquote", class_="postMessage")
        #    postInfoDesktopReply = postReply.find("div", class_="postInfo desktop")
        #    postNumDesktopReply = postInfoDesktopReply.find("span", class_="postNum desktop")
        #    noReply = postNumDesktopReply.find_all("a")
        #    print(color.colors.GREEN + "Anon" + color.colors.END + " No." + noReply[1].text)
        #    
        #    replyMessage = str(replyMessage).replace("</br>", "\n")
        #    replyMessage = str(replyMessage).replace("<br/>", "\n")
        #    replyMessage = BeautifulSoup(replyMessage, "html.parser")
        #    print(replyMessage.text.strip())
        #    print()

        print(str(i) + "/"+ str(len(threads)))
        enterThread = input()
        
        if enterThread == "a":
            os.system("clear")
            URL = ogURL+"thread/"+no[1].text
            pageThread = requests.get(URL)
            soupThread = BeautifulSoup(pageThread.content, "html.parser")
            
            delform = soupThread.find("form", {"name":"delform"})
            boardThread = delform.find("div", class_="board")
            threadThread = boardThread.find("div", class_="thread")
            postContainerOpThread = threadThread.find("div", class_="postContainer opContainer")
            postOpThread = postContainerOpThread.find("div", class_="post op")
            
            # subject
            postInfoDesktopThread = postOpThread.find("div", class_="postInfo desktop")
            subjectThread = postInfoDesktopThread.find("span", class_="subject")
            #check if there is a title
            if len(subjectThread) > 0:
                print(color.colors.BLUE + subjectThread.text.strip() + color.colors.END + "\n")
            else:
                print(color.colors.BLUE + "**no title**" + color.colors.END + "\n")
                
            # image
            fileThread = postOpThread.find("div", class_="file")
            fileThumbThread = fileThread.find("a", class_="fileThumb")
            if fileThumbThread:
                imgThread = fileThumbThread.find("img")
                imgThreadURL = img['src']
                imgThreadURL = "https:"+imgThreadURL
                imgThread_data = requests.get(imgThreadURL).content
                with open("Pic/picture"+str(i)+".jpg", 'wb') as handler:
                    handler.write(imgThread_data)
                imgThreadMagic = AsciiArt.from_image("Pic/picture"+str(i)+".jpg")
                imgThreadMagic.to_terminal(columns=40)
                print()
            
            
            # text
            postMessageThread = postOpThread.find("blockquote", class_="postMessage")
            postMessageThread = str(postMessageThread).replace("</br>", "\n")
            postMessageThread = str(postMessageThread).replace("<br/>", "\n")
            postMessageThread = BeautifulSoup(postMessageThread, "html.parser")
            print(postMessageThread.text.strip()+"\n")
            input()
