from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import os
from functions import accept_cookies, prepare_driver

# <div id="t1_jqi08v0" style="padding-left:37px" tabindex="-1" class="_3sf33-9rVAO_v4y0pIW_CH"><div class="_1DooEIX-1Nj5rweIc5cw_E"><div class="_36AIN2ppxy_z-XSDxTvYj5 t1_jqhvy6h"><i class="threadline"></i></div><div class="_3Wv3am0TXfTcugZJ6niui"><div class="_36AIN2ppxy_z-XSDxTvYj5 t1_jqi08v0 "><i class="threadline"></i></div></div></div><div class="Comment t1_jqi08v0 P8SGAKMtRxNwlmLz1zdJu HZ-cv9q391bm8s7qT54B3"><button class="_1nGapmdexvR0BuOkfAi6wa t1_jqi08v0 _1zN1-lYh2LfbYOMAho_O8g _2Gzh48SaLz7dQBCULfOC6V"><i class="icon icon-expand _1tnrhhM9S7dYjApTfvd14l"></i></button><div class="_2mHuuvyV9doV3zwbZPtIPG ZvAy-PJfJmB8pzQxpz1sS"><div id="AvatarUserInfoTooltip--t1_jqi08v0"><a class="_3GfQMgsm3HGd3838lwqCST" data-testid="comment_author_icon" href="/user/Leavingtheecstasy/"><div class="_2p14AQvJBvTrEEa4csiW9v _1TENjLYSaj4L4uJMZa3DRe"><div class="_3ppYbU2ZS369JSNSb8585I"></div><svg class="_1AX7t-EP7R4ZoVC41DG-Jx" fill="none" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><radialGradient id="a" cx="0" cy="0" gradientTransform="matrix(20.06268 6.0999 -3097.55815 10187.91225 -3.1 11.6)" gradientUnits="userSpaceOnUse" r="1"><stop offset="0" stop-color="#1185b5"></stop><stop offset=".29" stop-color="#d7f7ff"></stop><stop offset=".53" stop-color="#5ef6d8"></stop><stop offset=".84" stop-color="#5ef6d8"></stop><stop offset=".87" stop-color="#1990b9"></stop><stop offset="1" stop-color="#3f9fc6"></stop></radialGradient><path d="M13.77 1.1c.76-.41 1.7-.41 2.46 0L28 7.58c.75.42 1.2 1.17 1.2 1.96v12.94c0 .79-.45 1.54-1.2 1.95L16.23 30.9c-.76.42-1.7.42-2.46 0L2 24.42a2.25 2.25 0 0 1-1.2-1.95V9.53C.8 8.74 1.24 8 2 7.57z" stroke="url(#a)" stroke-linejoin="round" stroke-width="1.59"></path></svg><div class="_1cyAeeYDGrx7MPL_jRwKZ _13ScjOmi6dGdJw0JAonQEr  _3Bn5QwbgKslkdt4UwkP9r9"><div class="_2_QqG5dG916znjlVV8ZCbw"></div><div class="_1XJXnCAngvZLEeLpB3oa4L"><img alt="User avatar" class="ScrrUjzznpAqm92uwgnvO" src="https://styles.redditmedia.com/t5_ar6kg/styles/profileIcon_snoo-nftv2_bmZ0X2VpcDE1NToxMzdfYmZkNjcwNjY3MDUzZTUxN2E5N2FmZTU2YzkxZTRmODNmMTE2MGJkM181Mjg4_rare_d978abee-a101-400d-8bdb-b0ea72870289-headshot.png?width=256&amp;height=256&amp;crop=256:256,smart&amp;v=enabled&amp;s=72e539207fc39f9abc544d2627b0df75451466f1"></div></div><span></span></div></a></div></div><div class="_3tw__eCCe7j-epNCKGXUKk"><span class="_1RIl585IYPW6cmNXwgRz0J">level 2</span><div class="-Xcv3XBXmgiY2X5RqaPbO _1S45SPAIb30fsXtEcKPSdt _3LqBzV8aCO9tge99jHiUGy " data-testid="post-comment-header"><span class="_1a_HxF03jCyxnx706hQmJR"><div class="_3QEK34iVL1BjyHAVleVVNQ"><div class="_2mHuuvyV9doV3zwbZPtIPG"><div id="UserInfoTooltip--t1_jqi08v0"><a class="wM6scouPXXsFDSZmZPHRo DjcdNGtVXPcxG0yiFXIoZ _23wugcdiaj44hdfugIAlnX " data-testid="comment_author_link" href="/user/Leavingtheecstasy/">Leavingtheecstasy</a></div></div></div><span class="_3NdKulBcLHFmpKDAy9Barm _2a_XgY10KOzM0PRvywwDuY" data-testid="achievement-flairs"><img alt="Avid Voter" class="_2Xc055D-KCIUe6f2E3Ghgr" src="https://www.redditstatic.com/gold/achievement_flairs/upvoter_120.png"><span class="_1zxdGxj6UKKqJMibObCbeA">+1</span></span><span class="_2ETuFsVzMBxiHia6HfJCTQ _8b8fUdBRxCYj9MkNpFvvv"> · </span><a class="_3yx4Dn0W3Yunucf5sVJeFU" data-testid="comment_timestamp" href="https://www.reddit.com/r/wallstreetbets/comments/14pgsxe/comment/jqi08v0/?utm_source=reddit&amp;utm_medium=web2x&amp;context=3" id="CommentTopMeta--Created--t1_jqi08v0" target="_blank" rel="nofollow noopener noreferrer">3 hr. ago</a><div class="_3XoW0oYd5806XiOr24gGdb"></div></span></div><div data-testid="comment" class="_3cjCphgls6DH-irkVaA0GM "><div class="_292iotee39Lmt0MkQZ2hPV RichTextJSON-root"><p class="_1qeIAgB0cPwnLhDF9XSiJM">Mine burned in the dryer and I don't see how the fuck this makes more money</p></div></div><div class="_3KgrO85L1p9wQbgwG27q4y"><div class="_1E9mcoVn4MYnuBQSVDt1gC _2oM1YqCxIwkvwyeZamWwhW _1ewTEGuogtFmDvDII2T2Yy" id="vote-arrows-t1_jqi08v0"><button aria-label="upvote" aria-pressed="false" data-click-id="upvote" data-adclicklocation="upvote" class="_2k73nZrjAYiwAj9hv7K-kq  _22nWXKAY6OzAfK5GcUqWV2" style="--verticalvotes-customupvote-active:url(https://styles.redditmedia.com/t5_2th52/styles/postUpvoteIconActive_130uvmw23vb11.png);--verticalvotes-customupvote-inactive:url(https://styles.redditmedia.com/t5_2th52/styles/postUpvoteIconInactive_r8b8f7ke4vb11.png)"></button><div class="_1rZYMD_4xY3gRcSS3p8ODO _25IkBM0rRUqWX5ZojEMAFQ _3ChHiOyYyUkpZ_Nm3ZyM2M" style="color:#1A1A1B">64</div><button aria-label="downvote" aria-pressed="false" data-click-id="downvote" data-adclicklocation="downvote" class="ceU_3ot04pOVIcrrXH9fY  _783RL1AYIib59nxLCXhgv" style="--verticalvotes-customdownvote-active:url(https://styles.redditmedia.com/t5_2th52/styles/postDownvoteIconActive_lrmmpto33vb11.png);--verticalvotes-customdownvote-inactive:url(https://styles.redditmedia.com/t5_2th52/styles/postDownvoteIconInactive_20irq81e4vb11.png)"></button></div><div class="XZK-LTFT5CgGo9MvPQQsy _1LXnp2ufrzN6ioaTLTjGQ1 _2Ik7QEXtA-lbZKj0ssL89G _2hXOR2fIcfnUg0p-Env7KQ _3rHRwVOKmBBlBOQ4kIW_vq _2_lhaFUJdP8q0o2L9MN2TN"><button class="_374Hkkigy4E4srsI2WktEd"><i class="icon icon-comment _1g4YvNNIFoV_5_EhsVfyRy"></i>Reply</button><button class="_374Hkkigy4E4srsI2WktEd _2hr3tRWszeMRQ0u_Whs7t8 _14hLFU5cIJCyxH9DSgsCov">Give Award</button><div id="t1_jqi08v0-comment-share-menu"><button class="_374Hkkigy4E4srsI2WktEd">Share</button></div><button class="_374Hkkigy4E4srsI2WktEd _2hr3tRWszeMRQ0u_Whs7t8 _14hLFU5cIJCyxH9DSgsCov">Report</button><button class="_374Hkkigy4E4srsI2WktEd _2hr3tRWszeMRQ0u_Whs7t8 _14hLFU5cIJCyxH9DSgsCov">Save</button><button class="_374Hkkigy4E4srsI2WktEd _2hr3tRWszeMRQ0u_Whs7t8 _14hLFU5cIJCyxH9DSgsCov">Follow</button><div class="hrV8gUgmt0V7wM2wgZ81l _1YnPvd-E5MbmcM3PvRRcX _14hLFU5cIJCyxH9DSgsCov"><button aria-expanded="false" aria-haspopup="true" aria-label="more options" id="t1_jqi08v0-overflow-menu" data-adclicklocation="overflow_menu" class="_2pFdCpgBihIaYh9DSMWBIu _1VR6DV38j4rMT5OMeU4gJZ uMPgOFYlCc5uvpa2Lbteu"><i class="_38GxRFSqSC-Z2VLi5Xzkjy icon icon-overflow_horizontal"></i></button></div></div></div></div></div></div>


def screenshot_comments(comment_driver, link, post_counter):
    comment_driver.get(link)
    # Get all <div> elements and look for items with data_testid="post-container"
    comment_elements = comment_driver.find_elements(By.TAG_NAME, "shreddit-comment")
    comment_counter = 0
    for comment_element in comment_elements:
        try:
            thing_id = comment_element.get_attribute("thingid")
            parent_id = comment_element.get_attribute("parentid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")
        if len(thing_id) == 10 and parent_id is None:
            try:
                comment_element.screenshot(f"screenshots/comments/post_{post_counter}_comment{comment_counter}.png", )
                comment_counter += 1
            except WebDriverException:
                print("------------ This element is not visible")
        if comment_counter == 5:
            print(f"{comment_counter} comments were extracted")
            break



def go_to_comments(element):
    children = element.find_elements(By.TAG_NAME, "a")
    for child in children:
        comments_link = child.get_attribute("href")
        if "comments" in comments_link:
            return comments_link


# Delete existing screenshots
screenshot_path = "screenshots"
sub_paths = ["posts", "comments"]
for sub_path in sub_paths:
    dir_path = f"{screenshot_path}/{sub_path}"
    files = os.listdir(dir_path)
    for file in files:
        if "init" not in file:
            os.remove(f"{dir_path}/{file}")

# Set chromedriver options
driver = prepare_driver()
comments_driver = prepare_driver()

# Point driver to URL
driver.get("https://www.reddit.com/r/wallstreetbets/hot/")

# Accept cookies
accept_cookies(driver)


def func1(driver, comments_driver):
    # Get all <div> elements and look for items with data_testid="post-container"
    elements = driver.find_elements(By.TAG_NAME, "div")
    counter = 0
    for element in elements:
        try:
            data_testid = element.get_attribute("data-testid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")
        if "post-container" == data_testid:
            try:
                element.screenshot(f"screenshots/posts/post_{counter}.png", )
                comments_link = go_to_comments(element)
                comments_driver.switch_to.window(comments_driver.current_window_handle)
                screenshot_comments(comments_driver, comments_link, counter)
                driver.switch_to.window(driver.current_window_handle)
                counter += 1
            except WebDriverException:
                print("------------ This element is not visible")


func1(driver, comments_driver)
