"""START"""

# Import required modules
import datetime
import praw
import random
import time
import tkinter


# Defining time
now = datetime.datetime.now()
'''BOT'''


def bot():

    # BobRossBot_ v2.5 (cleaned up code, added youtube videos)
    # Created by /u/whaliam
    # 6Ep96ck9@protonmail.com
    # Create Reddit instance
    # Setting variables
    print("Logging in...")

    reddit = praw.Reddit(user_agent='<User_Agent>',  # A brief description of your bot! <#
                         client_id='<API_Public_Key>',  # Your API public key
                         client_secret='(API_Secret_key>',  # Your API private key
                         username='<Username>',  # Your Reddit username
                         password='<Password>')  # Your Reddit password

    print("Welcome BobRossBot_ :)")
    print("Started: " + str(now))
    print("Loading quotes...")
    '''BOT|QUOTES'''  # Enter quotes in the array below
    ross_quotes = \
        [
            " 'Trees cover up a multitude of sins.'",

            " 'Remember our Golden Rule: A thin paint sticks to a thick paint.' ",

            " 'And that makes it look like birch trees, isn't that sneaky? Heh. Ha. It's gorgeous.' ",

            " 'Be sure to use odorless paint-thinner. If it's not odorless, you'll find yourself working alone very, "
            "very quick.' ",

            " 'Let's just blend this little rascal here, ha! Happy as we can be.' ",

            " 'Clouds are very, very free.' ",

            " 'Decide where your little footy hills live.' ",

            " 'Shwooop. Hehe. You have to make those little noises, or it just doesn't work.' ",

            " 'Try to imagine that you are a tree. How do you want to look out here?' ",

            "  'You know me, I gotta put in a big tree.' ",

            " 'Gotta give him a friend. Like I always say 'everyone needs a friend'. ",

            "  'Any time ya learn, ya gain.' ",

            "  'Just put a few do-ers in there...' ",

            "  'Maybe in our world there lives a happy little tree over there.' ",

            "  'You can do anything you want to do. This is your world.' ",

            "  'You can put as many or as few as you want in your world.' ",

            " 'That's a crooked tree. We'll send him to Washington.' ",

            " 'I like to beat the brush.' ",

            " 'In painting, you have unlimited power. You have the ability to move mountains. You can bend rivers. But "
            "when I get home, the only thing I have power over is the garbage.' ",

            " 'You need the dark in order to show the light.' ",

            " 'Look around. Look at what we have. Beauty is everywhere—you only have to look to see it.' ",

            " 'There's nothing wrong with having a tree as a friend.' ",

            " 'There's nothing wrong with having a tree as a friend.' ",

            " 'They say everything looks better with odd numbers of things. But sometimes I put even numbers—just to "
            "upset the critics.' ",

            " 'How do you make a round circle with a square knife? That’s your challenge for the day.' ",

            " 'I remember when my Dad told me as a kid, ‘If you want to catch a rabbit, stand behind a tree and make a "
            "noise like a carrot. Then when the rabbit comes by you grab him.’ Works pretty good until you try to "
            "figure out what kind of noise a carrot makes…' ",

            " 'We tell people sometimes: we're like drug dealers, come into town and get everybody absolutely addicted "
            "to painting. It doesn't take much to get you addicted.' ",

            " 'The secret to doing anything is believing that you can do it. Anything that you believe you can do "
            "strong enough, you can do. Anything. As long as you believe. ",

            " 'Water's like me. It's laaazy ... Boy, it always looks for the easiest way to do things' ",

            " 'Oooh, if you have never been to Alaska, go there while it is still wild. My favorite uncle asked me if "
            "I wanted to go there, Uncle Sam. He said if you don't go, you're going to jail. That is how Uncle Sam "
            "asks you.' ",

            " 'I really believe that if you practice enough you could paint the 'Mona Lisa' with a two-inch brush.' ",

            " 'If I paint something, I don't want to have to explain what it is.' ",

            " 'We artists are a different breed of people. We're a happy bunch.' ",

            " 'We don't make mistakes. We just have happy accidents.' ",

            " 'We don't make mistakes. We just have happy accidents.' ",

            " 'You too can paint almighty pictures.' ",

            " 'Don’t forget to make all these little things individuals — all of them special in their own way.' ",

            " 'Talent is a pursued interest. Anything that you’re willing to practice, you can do.' ",

            " 'Make love to the canvas.' ",

            " 'Don’t forget to tell these special people in your life just how special they are to you.' ",

            " 'Just let go — and fall like a little waterfall.' ",

            " 'You can do anything you want to do. This is your world.' ",

            " 'You can have anything you want in the world — once you help everyone around you get what they want.' ",

            " 'If you do too much, it’s going to lose its effectiveness.' ",

            " 'This is happy place; little squirrels live here and play.' ",

            " 'Remember how free clouds are. They just lay around in the sky all day long' ",

            " 'That’s where the crows will sit. But we’ll have to put an elevator to put them up there because they "
            "can’t fly, but they don’t know that, so they still try.' ",

            " 'We don’t really know where this goes — and I’m not sure we really care.' ",

            " 'Go out on a limb — that’s where the fruit is.' ",

            " 'Isn’t it fantastic that you can change your mind and create all these happy things?' ",

            " 'It’s life. It’s interesting. It’s fun.' ",

        ]
    '''BOT|IMAGES'''  # Enter Imgur links in the array below

    image_urls = ['gallery/q2GEp', 'gallery/XJUfQ', 'gallery/L0rLs', 'gallery/m58x4xS', 'gallery/r6xblZg',
                  'gallery/mT1DRVY', 'gallery/Xy1sA', 'gallery/hc3HO', 'gallery/3Xfh1', 'gallery/8USdT',
                  'gallery/CE5blh5', 'gallery/m7ymyYp', 'gallery/2ECwjYr', 'gallery/kK1Zr', 'gallery/qs6Xd',
                  'gallery/DJ4zL', 'gallery/xWBUI8S', 'gallery/hM7ls6K', 'gallery/P6L9y', 'a/BP7kB', 'gyuNg8j.jpg',
                  '7RmtwPK', 'sgJbHNS.jpg', 'a/tMF0C', '1qytrLH.jpg', 'BezhUOU.jpg', 'gallery/fzQkm', 'a/jSPlu',
                  'a/e01ND', 'a/oeGZ6', 'w4nER2N', '7b44qgF.jpg', '7b44qgF.jpg', 'L48F2T6', 'iYytETj']
    ross_images = []
    for url in image_urls:
        message = ' [Here\'s a random painting :)](https://imgur.com/%s) ' % url
        ross_images.append(message)

    '''YOUTUBE URLS'''
    youtube_urls = ['lLWEXRAnQd0', 'VlucWfTUo1A', 'dNEp3hoHSDI', 'oh5p5f5_-7A', 'kasGRkfkiPM', 'pw5ETGiiBRg',
                    'L5bXkI0-pEg', 'I-ousb8-SD0', 'UQ-RTZCOQn0', 'BW2wKKFvH1g', 'XZmdzfvXRuw', 'vgbMONXc9Cs',
                    'HCsCatvigtw', 'enutOy-nsZk', 'LygUyAb78oY', 'VnZEpic2UzU', 'zxj3xLDNxo0', 'PutvF_P4588',
                    '8ysFkNYwhAE', 'qTDQt_PdlYc', 'kJFB6rH3z2A', 'TohG7F8M3Ls', 'DFSIQNjKRfk', 'nJGCVFn57U8',
                    'IEQWfszfRlA', 'mEU0stNfkxI', 'RInDWhYceLU', '0FYfo94qefg', 'qx2IsmrCs3c', 'qXElmiqzcI0',
                    'DFQlu6eqrBo', 'MHJB0IBnuD4', 'OFKFUJ9eDNs', 'Ugiwi8uizpg', '4KYxkqlzyqM', 'Qj6lMtnCt8o',
                    'wrbGlR22K0Q', 'RrBsbqO9aqI', 'eTEKGOi6SVg', 'GzSqjyQUPZQ', 'O6L5YPt9CeU', 'zoTeyliLn5o',
                    'aA8RhtaWACA', 'Da4SPyh1ATM', 'uEUMVwc4o5U', 'UOziR7PoVco', 'vrAMRxBB5KI', 'NcVeRlPu_5w',
                    'Vx6v47gHBWM', 'OJ_xqtvZf3o', '8P-YeoTmVrw', '1s58rW0_LN4', 'lzODyJS2ZIg', 'Wj-3ct7RvAI',
                    'KYlM2zJnNWY', 'DqhzxdkdQS0', 'jfCsew_mz7A', 'gMEZp47VKC0', 'iRMsb9Vf7GM', '4XxClvPZ1RE',
                    'fBh1nA4pMDY', 'loAzRUzx1wI', 'AGhXEPfp-W4', 'GhOGZMpPUSE', 'tWoInh2USOs', '530_cVmexiI',
                    '6evqNlOO7Bw', 'o2cjLA_wgIk', 'miJ19Kz_i3Y', 'OHSm8kLE7js', 'kNZssD9zWlw', 'RqtDliGeyTg',
                    'lSeRrm5ZK9c', 'puGk2iFvvp0', 'EVQcDEiJh2o', '0pwoixRikn4']
    youtube_links = []
    for url in youtube_urls:
        message = ' [Here\'s a link to a random video of me painting](https://youtube.com/watch?v=%s)' % url
        youtube_links.append(message)

    '''BOT|REDIRECT URLS'''  # Enter Redirect/Information URL(S) in the strings below
    code = "|| [code](https://github.com/whaliam/BobRossBot) ||💻[feedback](https://www.reddit.com/user/'" \
           "BobRossBot_/comments/7ikvn5/feedback_3_and_code/)"

    # Set subreddit parameters
    subreddit = reddit.subreddit("all")

    print("Searching for instances of 'Bob Ross...'")

    # Set comment parameters
    for comment in subreddit.stream.comments():

        if tkinter.re.search("bob ross", comment.body, tkinter.re.IGNORECASE):
            ross_reply = random.choice(ross_quotes) + str("||") + random.choice(youtube_links) + str("||") \
                         + random.choice(ross_images)
            print("comment found!")
            print("preparing quote")
            comment.reply(ross_reply + code)
            print("replied with quote!")
            print("starting cooldown")
            print("cooldown")
            print(str(now))
            print(str(comment.reply))
            time.sleep(10)

    # Created by /u/whaliam
    # 6Ep96ck9@protonmail.com


'''GUI'''
# Start GUI

'''GUI|MAINMENU'''

# Create main window
root = tkinter.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)
'''GUI|SUBMENU(S)'''

# Create menu
# First submenu
submenu = tkinter.Menu(menu)
menu.add_cascade(label="Bot", menu=submenu)
submenu.add_separator()
submenu.add_command(label="Start Bot", command=bot)
submenu.add_separator()
# Second submenu
submenu2 = tkinter.Menu(root)
menu.add_cascade(label="Settings", menu=submenu2)
submenu2.add_separator()
submenu2.add_command(label="Exit", command=exit)
submenu2.add_separator()

# Loop GUI
root.mainloop()

'''END'''

