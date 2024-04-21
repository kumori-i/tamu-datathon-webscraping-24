# https://webscrape4-dot-chunin.uc.r.appspot.com/login
# username: 1234
# password: s3lenium!


import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Launch the browser
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://webscrape4-dot-chunin.uc.r.appspot.com/login")

# Enter the ID Number
id_input = driver.find_element(By.NAME, "id_no")
id_input.send_keys("1234")

# Enter the password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("s3lenium!")

# Click the login button
login_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']")
login_button.click()

time.sleep(2)

# Wait for the login to complete
driver.implicitly_wait(5)  # Adjust the wait time as needed

# Navigate to the webpage after login
driver.get("https://webscrape4-dot-chunin.uc.r.appspot.com/scrape")

# time.sleep(5)

# # Wait for the content to load
# posts = driver.find_elements(By.CLASS_NAME, "post")
#

print("Scrolling down to load all posts...")
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Wait for a moment after scrolling
time.sleep(1)

# Get all posts
posts = driver.find_elements(By.CLASS_NAME, "post")

# Get the rating
for post in posts:
    # Get the rating
    rating_element = post.find_element(By.XPATH, ".//p[contains(., 'Rating:')]")
    rating_text = rating_element.text.split(":")[-1].strip()
    rating = int(rating_text)

    # Determine comment based on rating
    if rating == 5:
        comment = "Thank you for the great review! We hope to see you again soon!"
    elif rating == 4:
        comment = "Thanks for the positive feedback! We'll keep it up."
    elif rating == 3:
        comment = "Appreciate your feedback! We'll work on areas needing improvement."
    elif rating == 2:
        comment = "Thanks for your feedback. We'll use it to improve. Any specific suggestions?"
    else:
        comment = "We're sorry to hear about your experience. Could you share more details so we can address your concerns?"

    # Fill in the comment input field
    comment_input = post.find_element(By.CLASS_NAME, "comment-input")
    comment_input.send_keys(comment)

    # Click the post comment button
    post_comment_button = post.find_element(By.CLASS_NAME, "post-comment")
    post_comment_button.click()

    # Wait for a while to see the result
    # print("Comment posted for a post with rating:", rating)
    # time.sleep(2)  # Adjust the wait time as needed

flag_pattern = re.compile(r"flag\{([^}]*)\}")
matches = flag_pattern.findall(driver.page_source)
if matches:
    for match in matches:
        print("Flag found:", match)
else:
    print("Flag not found.")

# Close the browser
print("Closing the browser...")
driver.quit()

    # first log in html
    # <html lang="en"><script src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/content/fido2/page-script.js" id="bw-fido2-page-script"></script><head>
    #             <meta charset="UTF-8">
    #             <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #             <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #             <title>Login</title>
    #         <style>
    #         body {
    #             font-family: Arial, sans-serif;
    #             background-color: #f4f4f4;
    #             margin: 0;
    #             padding: 0;
    #             display: flex;
    #             justify-content: center;
    #             align-items: center;
    #             height: 100vh;
    #         }
    #         form {
    #             background-color: #fff;
    #             padding: 20px;
    #             border-radius: 8px;
    #             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    #         }
    #         label {
    #             display: block;
    #             margin-bottom: 10px;
    #         }
    #         select, input[type="text"], input[type="password"] {
    #             width: 100%;
    #             padding: 8px;
    #             margin-bottom: 15px;
    #             border: 1px solid #ccc;
    #             border-radius: 4px;
    #             box-sizing: border-box;
    #         }
    #         input[type="submit"] {
    #             width: 100%;
    #             background-color: #007bff;
    #             color: #fff;
    #             padding: 10px;
    #             border: none;
    #             border-radius: 4px;
    #             cursor: pointer;
    #             font-size: 16px;
    #         }
    #         input[type="submit"]:hover {
    #             background-color: #0056b3;
    #         }
    #         </style><link href="data:text/css,%3Ais(%5Bid*%3D'google_ads_iframe'%5D%2C%5Bid*%3D'taboola-'%5D%2C.taboolaHeight%2C.taboola-placeholder%2C%23credential_picker_container%2C%23credentials-picker-container%2C%23credential_picker_iframe%2C%5Bid*%3D'google-one-tap-iframe'%5D%2C%23google-one-tap-popup-container%2C.google-one-tap-modal-div%2C%23amp_floatingAdDiv%2C%23ez-content-blocker-container)%20%7Bdisplay%3Anone!important%3Bmin-height%3A0!important%3Bheight%3A0!important%3B%7D" rel="stylesheet" type="text/css"><style>.rdp {
    # --rdp-cell-size: 40px;
    # --rdp-accent-color: #0000ff;
    # --rdp-background-color: #e7edff;
    # --rdp-accent-color-dark: #3003e1;
    # --rdp-background-color-dark: #180270;
    # --rdp-outline: 2px solid var(--rdp-accent-color); /* Outline border for focused elements */
    # --rdp-outline-selected: 2px solid rgba(0, 0, 0, 0.75); /* Outline border for focused _and_ selected elements */

    # margin: 1em;
    # }

    # /* Hide elements for devices that are not screen readers */
    # .rdp-vhidden {
    # box-sizing: border-box;
    # padding: 0;
    # margin: 0;
    # background: transparent;
    # border: 0;
    # -moz-appearance: none;
    # -webkit-appearance: none;
    # appearance: none;
    # position: absolute !important;
    # top: 0;
    # width: 1px !important;
    # height: 1px !important;
    # padding: 0 !important;
    # overflow: hidden !important;
    # clip: rect(1px, 1px, 1px, 1px) !important;
    # border: 0 !important;
    # }

    # /* Buttons */
    # .rdp-button_reset {
    # appearance: none;
    # position: relative;
    # margin: 0;
    # padding: 0;
    # cursor: default;
    # color: inherit;
    # outline: none;
    # background: none;
    # font: inherit;

    # -moz-appearance: none;
    # -webkit-appearance: none;
    # }

    # .rdp-button {
    # border: 2px solid transparent;
    # }

    # .rdp-button[disabled] {
    # opacity: 0.25;
    # }

    # .rdp-button:not([disabled]) {
    # cursor: pointer;
    # }

    # .rdp-button:focus:not([disabled]),
    # .rdp-button:active:not([disabled]) {
    # color: inherit;
    # border: var(--rdp-outline);
    # background-color: var(--rdp-background-color);
    # }

    # .rdp-button:hover:not([disabled]) {
    # background-color: var(--rdp-background-color);
    # }

    # .rdp-months {
    # display: flex;
    # }

    # .rdp-month {
    # margin: 0 1em;
    # }

    # .rdp-month:first-child {
    # margin-left: 0;
    # }

    # .rdp-month:last-child {
    # margin-right: 0;
    # }

    # .rdp-table {
    # margin: 0;
    # max-width: calc(var(--rdp-cell-size) * 7);
    # border-collapse: collapse;
    # }

    # .rdp-with_weeknumber .rdp-table {
    # max-width: calc(var(--rdp-cell-size) * 8);
    # border-collapse: collapse;
    # }

    # .rdp-caption {
    # display: flex;
    # align-items: center;
    # justify-content: space-between;
    # padding: 0;
    # text-align: left;
    # }

    # .rdp-multiple_months .rdp-caption {
    # position: relative;
    # display: block;
    # text-align: center;
    # }

    # .rdp-caption_dropdowns {
    # position: relative;
    # display: inline-flex;
    # }

    # .rdp-caption_label {
    # position: relative;
    # z-index: 1;
    # display: inline-flex;
    # align-items: center;
    # margin: 0;
    # padding: 0 0.25em;
    # white-space: nowrap;
    # color: currentColor;
    # border: 0;
    # border: 2px solid transparent;
    # font-family: inherit;
    # font-size: 140%;
    # font-weight: bold;
    # }

    # .rdp-nav {
    # white-space: nowrap;
    # }

    # .rdp-multiple_months .rdp-caption_start .rdp-nav {
    # position: absolute;
    # top: 50%;
    # left: 0;
    # transform: translateY(-50%);
    # }

    # .rdp-multiple_months .rdp-caption_end .rdp-nav {
    # position: absolute;
    # top: 50%;
    # right: 0;
    # transform: translateY(-50%);
    # }

    # .rdp-nav_button {
    # display: inline-flex;
    # align-items: center;
    # justify-content: center;
    # width: var(--rdp-cell-size);
    # height: var(--rdp-cell-size);
    # padding: 0.25em;
    # border-radius: 100%;
    # }

    # /* ---------- */
    # /* Dropdowns  */
    # /* ---------- */

    # .rdp-dropdown_year,
    # .rdp-dropdown_month {
    # position: relative;
    # display: inline-flex;
    # align-items: center;
    # }

    # .rdp-dropdown {
    # appearance: none;
    # position: absolute;
    # z-index: 2;
    # top: 0;
    # bottom: 0;
    # left: 0;
    # width: 100%;
    # margin: 0;
    # padding: 0;
    # cursor: inherit;
    # opacity: 0;
    # border: none;
    # background-color: transparent;
    # font-family: inherit;
    # font-size: inherit;
    # line-height: inherit;
    # }

    # .rdp-dropdown[disabled] {
    # opacity: unset;
    # color: unset;
    # }

    # .rdp-dropdown:focus:not([disabled]) + .rdp-caption_label,
    # .rdp-dropdown:active:not([disabled]) + .rdp-caption_label {
    # border: var(--rdp-outline);
    # border-radius: 6px;
    # background-color: var(--rdp-background-color);
    # }

    # .rdp-dropdown_icon {
    # margin: 0 0 0 5px;
    # }

    # .rdp-head {
    # border: 0;
    # }

    # .rdp-head_row,
    # .rdp-row {
    # height: 100%;
    # }

    # .rdp-head_cell {
    # vertical-align: middle;
    # text-transform: uppercase;
    # font-size: 0.75em;
    # font-weight: 700;
    # text-align: center;
    # height: 100%;
    # height: var(--rdp-cell-size);
    # padding: 0;
    # }

    # .rdp-tbody {
    # border: 0;
    # }

    # .rdp-tfoot {
    # margin: 0.5em;
    # }

    # .rdp-cell {
    # width: var(--rdp-cell-size);
    # height: 100%;
    # height: var(--rdp-cell-size);
    # padding: 0;
    # text-align: center;
    # }

    # .rdp-weeknumber {
    # font-size: 0.75em;
    # }

    # .rdp-weeknumber,
    # .rdp-day {
    # display: flex;
    # overflow: hidden;
    # align-items: center;
    # justify-content: center;
    # box-sizing: border-box;
    # width: var(--rdp-cell-size);
    # max-width: var(--rdp-cell-size);
    # height: var(--rdp-cell-size);
    # margin: 0;
    # border: 2px solid transparent;
    # border-radius: 100%;
    # }

    # .rdp-day_today:not(.rdp-day_outside) {
    # font-weight: bold;
    # }

    # .rdp-day_selected:not([disabled]),
    # .rdp-day_selected:focus:not([disabled]),
    # .rdp-day_selected:active:not([disabled]),
    # .rdp-day_selected:hover:not([disabled]) {
    # color: white;
    # background-color: var(--rdp-accent-color);
    # }

    # .rdp-day_selected:focus:not([disabled]) {
    # border: var(--rdp-outline-selected);
    # }

    # .rdp:not([dir='rtl']) .rdp-day_range_start:not(.rdp-day_range_end) {
    # border-top-right-radius: 0;
    # border-bottom-right-radius: 0;
    # }

    # .rdp:not([dir='rtl']) .rdp-day_range_end:not(.rdp-day_range_start) {
    # border-top-left-radius: 0;
    # border-bottom-left-radius: 0;
    # }

    # .rdp[dir='rtl'] .rdp-day_range_start:not(.rdp-day_range_end) {
    # border-top-left-radius: 0;
    # border-bottom-left-radius: 0;
    # }

    # .rdp[dir='rtl'] .rdp-day_range_end:not(.rdp-day_range_start) {
    # border-top-right-radius: 0;
    # border-bottom-right-radius: 0;
    # }

    # .rdp-day_range_end.rdp-day_range_start {
    # border-radius: 100%;
    # }

    # .rdp-day_range_middle {
    # border-radius: 0;
    # }
    # </style></head>

    #         <body class="vsc-initialized">
    #             <div>
    #                 <form action="/login" method="post" data-bitwarden-watching="1">
    #                     <label for="user_type">User Type:</label>
    #                     <select name="user_type">
    #                         <option value="admin">Admin</option>
    #                         <option value="user">User</option>
    #                     </select>
    #                     <label for="id_no">ID Number:</label>
    #                     <input type="text" name="id_no">
    #                     <label for="password">Password:</label>
    #                     <input type="password" name="password">
    #                     <input type="submit" value="Login">
    #                 </form>
    #             </div>


    #     </body></html>
    #
    #
    #
    # second html
    # <html lang="en"><head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Datathon Starbucks</title>
    #     <link rel="stylesheet" href="scrape.css">
    # <script src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/content/fido2/page-script.js" id="bw-fido2-page-script"></script><link href="data:text/css,%3Ais(%5Bid*%3D'google_ads_iframe'%5D%2C%5Bid*%3D'taboola-'%5D%2C.taboolaHeight%2C.taboola-placeholder%2C%23credential_picker_container%2C%23credentials-picker-container%2C%23credential_picker_iframe%2C%5Bid*%3D'google-one-tap-iframe'%5D%2C%23google-one-tap-popup-container%2C.google-one-tap-modal-div%2C%23amp_floatingAdDiv%2C%23ez-content-blocker-container)%20%7Bdisplay%3Anone!important%3Bmin-height%3A0!important%3Bheight%3A0!important%3B%7D" rel="stylesheet" type="text/css"><style>.rdp {
    #   --rdp-cell-size: 40px;
    #   --rdp-accent-color: #0000ff;
    #   --rdp-background-color: #e7edff;
    #   --rdp-accent-color-dark: #3003e1;
    #   --rdp-background-color-dark: #180270;
    #   --rdp-outline: 2px solid var(--rdp-accent-color); /* Outline border for focused elements */
    #   --rdp-outline-selected: 2px solid rgba(0, 0, 0, 0.75); /* Outline border for focused _and_ selected elements */

    #   margin: 1em;
    # }

    # /* Hide elements for devices that are not screen readers */
    # .rdp-vhidden {
    #   box-sizing: border-box;
    #   padding: 0;
    #   margin: 0;
    #   background: transparent;
    #   border: 0;
    #   -moz-appearance: none;
    #   -webkit-appearance: none;
    #   appearance: none;
    #   position: absolute !important;
    #   top: 0;
    #   width: 1px !important;
    #   height: 1px !important;
    #   padding: 0 !important;
    #   overflow: hidden !important;
    #   clip: rect(1px, 1px, 1px, 1px) !important;
    #   border: 0 !important;
    # }

    # /* Buttons */
    # .rdp-button_reset {
    #   appearance: none;
    #   position: relative;
    #   margin: 0;
    #   padding: 0;
    #   cursor: default;
    #   color: inherit;
    #   outline: none;
    #   background: none;
    #   font: inherit;

    #   -moz-appearance: none;
    #   -webkit-appearance: none;
    # }

    # .rdp-button {
    #   border: 2px solid transparent;
    # }

    # .rdp-button[disabled] {
    #   opacity: 0.25;
    # }

    # .rdp-button:not([disabled]) {
    #   cursor: pointer;
    # }

    # .rdp-button:focus:not([disabled]),
    # .rdp-button:active:not([disabled]) {
    #   color: inherit;
    #   border: var(--rdp-outline);
    #   background-color: var(--rdp-background-color);
    # }

    # .rdp-button:hover:not([disabled]) {
    #   background-color: var(--rdp-background-color);
    # }

    # .rdp-months {
    #   display: flex;
    # }

    # .rdp-month {
    #   margin: 0 1em;
    # }

    # .rdp-month:first-child {
    #   margin-left: 0;
    # }

    # .rdp-month:last-child {
    #   margin-right: 0;
    # }

    # .rdp-table {
    #   margin: 0;
    #   max-width: calc(var(--rdp-cell-size) * 7);
    #   border-collapse: collapse;
    # }

    # .rdp-with_weeknumber .rdp-table {
    #   max-width: calc(var(--rdp-cell-size) * 8);
    #   border-collapse: collapse;
    # }

    # .rdp-caption {
    #   display: flex;
    #   align-items: center;
    #   justify-content: space-between;
    #   padding: 0;
    #   text-align: left;
    # }

    # .rdp-multiple_months .rdp-caption {
    #   position: relative;
    #   display: block;
    #   text-align: center;
    # }

    # .rdp-caption_dropdowns {
    #   position: relative;
    #   display: inline-flex;
    # }

    # .rdp-caption_label {
    #   position: relative;
    #   z-index: 1;
    #   display: inline-flex;
    #   align-items: center;
    #   margin: 0;
    #   padding: 0 0.25em;
    #   white-space: nowrap;
    #   color: currentColor;
    #   border: 0;
    #   border: 2px solid transparent;
    #   font-family: inherit;
    #   font-size: 140%;
    #   font-weight: bold;
    # }

    # .rdp-nav {
    #   white-space: nowrap;
    # }

    # .rdp-multiple_months .rdp-caption_start .rdp-nav {
    #   position: absolute;
    #   top: 50%;
    #   left: 0;
    #   transform: translateY(-50%);
    # }

    # .rdp-multiple_months .rdp-caption_end .rdp-nav {
    #   position: absolute;
    #   top: 50%;
    #   right: 0;
    #   transform: translateY(-50%);
    # }

    # .rdp-nav_button {
    #   display: inline-flex;
    #   align-items: center;
    #   justify-content: center;
    #   width: var(--rdp-cell-size);
    #   height: var(--rdp-cell-size);
    #   padding: 0.25em;
    #   border-radius: 100%;
    # }

    # /* ---------- */
    # /* Dropdowns  */
    # /* ---------- */

    # .rdp-dropdown_year,
    # .rdp-dropdown_month {
    #   position: relative;
    #   display: inline-flex;
    #   align-items: center;
    # }

    # .rdp-dropdown {
    #   appearance: none;
    #   position: absolute;
    #   z-index: 2;
    #   top: 0;
    #   bottom: 0;
    #   left: 0;
    #   width: 100%;
    #   margin: 0;
    #   padding: 0;
    #   cursor: inherit;
    #   opacity: 0;
    #   border: none;
    #   background-color: transparent;
    #   font-family: inherit;
    #   font-size: inherit;
    #   line-height: inherit;
    # }

    # .rdp-dropdown[disabled] {
    #   opacity: unset;
    #   color: unset;
    # }

    # .rdp-dropdown:focus:not([disabled]) + .rdp-caption_label,
    # .rdp-dropdown:active:not([disabled]) + .rdp-caption_label {
    #   border: var(--rdp-outline);
    #   border-radius: 6px;
    #   background-color: var(--rdp-background-color);
    # }

    # .rdp-dropdown_icon {
    #   margin: 0 0 0 5px;
    # }

    # .rdp-head {
    #   border: 0;
    # }

    # .rdp-head_row,
    # .rdp-row {
    #   height: 100%;
    # }

    # .rdp-head_cell {
    #   vertical-align: middle;
    #   text-transform: uppercase;
    #   font-size: 0.75em;
    #   font-weight: 700;
    #   text-align: center;
    #   height: 100%;
    #   height: var(--rdp-cell-size);
    #   padding: 0;
    # }

    # .rdp-tbody {
    #   border: 0;
    # }

    # .rdp-tfoot {
    #   margin: 0.5em;
    # }

    # .rdp-cell {
    #   width: var(--rdp-cell-size);
    #   height: 100%;
    #   height: var(--rdp-cell-size);
    #   padding: 0;
    #   text-align: center;
    # }

    # .rdp-weeknumber {
    #   font-size: 0.75em;
    # }

    # .rdp-weeknumber,
    # .rdp-day {
    #   display: flex;
    #   overflow: hidden;
    #   align-items: center;
    #   justify-content: center;
    #   box-sizing: border-box;
    #   width: var(--rdp-cell-size);
    #   max-width: var(--rdp-cell-size);
    #   height: var(--rdp-cell-size);
    #   margin: 0;
    #   border: 2px solid transparent;
    #   border-radius: 100%;
    # }

    # .rdp-day_today:not(.rdp-day_outside) {
    #   font-weight: bold;
    # }

    # .rdp-day_selected:not([disabled]),
    # .rdp-day_selected:focus:not([disabled]),
    # .rdp-day_selected:active:not([disabled]),
    # .rdp-day_selected:hover:not([disabled]) {
    #   color: white;
    #   background-color: var(--rdp-accent-color);
    # }

    # .rdp-day_selected:focus:not([disabled]) {
    #   border: var(--rdp-outline-selected);
    # }

    # .rdp:not([dir='rtl']) .rdp-day_range_start:not(.rdp-day_range_end) {
    #   border-top-right-radius: 0;
    #   border-bottom-right-radius: 0;
    # }

    # .rdp:not([dir='rtl']) .rdp-day_range_end:not(.rdp-day_range_start) {
    #   border-top-left-radius: 0;
    #   border-bottom-left-radius: 0;
    # }

    # .rdp[dir='rtl'] .rdp-day_range_start:not(.rdp-day_range_end) {
    #   border-top-left-radius: 0;
    #   border-bottom-left-radius: 0;
    # }

    # .rdp[dir='rtl'] .rdp-day_range_end:not(.rdp-day_range_start) {
    #   border-top-right-radius: 0;
    #   border-bottom-right-radius: 0;
    # }

    # .rdp-day_range_end.rdp-day_range_start {
    #   border-radius: 100%;
    # }

    # .rdp-day_range_middle {
    #   border-radius: 0;
    # }
    # </style></head>
    # <body class="vsc-initialized"><div id="bit-notification-bar-spacer" style="height: 42px;"></div>
    #     <div id="post-container"><div class="post">
    #           <h2>0 - Rude people with elder man </h2>
    #           <p><strong>Published Date:</strong> 1/7/2024</p>
    #           <p><strong>User says:</strong> Really rude people on the counter, they bully an elder man because was sit on a place that was not supposed to be for sitting! Wtf </p>
    #           <p><strong>Rating:</strong> 1</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>1 - Pausa caffè</h2>
    #           <p><strong>Published Date:</strong> 11/17/2023</p>
    #           <p><strong>User says:</strong> Per me che sono un amante dell’espresso, il caffè bibitone americano non è il massimo. Buona la brioche, utile come merenda per ricaricare le pile durante le lunghe camminate in città. Gentile il personale. </p>
    #           <p><strong>Rating:</strong> 3</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>2 - Meglio il Chai del Matcha</h2>
    #           <p><strong>Published Date:</strong> 9/4/2023</p>
    #           <p><strong>User says:</strong> In questa vacanza ho evitato questa catena (qui a NY ce n’è una quantità esagerata) cercando di privilegiare locali più caratteristici o del posto. Unica eccezione quando, zona Battery Park, ho avuto voglia di provare il Chai Latte. Devo dire che lo preferisco al Matcha Latte.</p>
    #           <p><strong>Rating:</strong> 3</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>3 - Colazione a New York</h2>
    #           <p><strong>Published Date:</strong> 8/15/2023</p>
    #           <p><strong>User says:</strong> Code infinite per cappuccino e brioche .Disorganizzazione per preparare la gestione degli ordini da app……….40 minuti per un cappuccino e muffin pazzesco!!!!!!</p>
    #           <p><strong>Rating:</strong> 1</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>4 - Great Location</h2>
    #           <p><strong>Published Date:</strong> 9/7/2022</p>
    #           <p><strong>User says:</strong> This is a good place to get coffee and sit on Times Square and people watch. There is no lack of entertainment.</p>
    #           <p><strong>Rating:</strong> 4</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>5 - There never disappoint </h2>
    #           <p><strong>Published Date:</strong> 6/29/2022</p>
    #           <p><strong>User says:</strong> I always love it here friendly staffs, great atmosphere, there never disappoint and the customer service is great even when they're crowded .</p>
    #           <p><strong>Rating:</strong> 4</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>6 - Schlechter Laden</h2>
    #           <p><strong>Published Date:</strong> 4/16/2022</p>
    #           <p><strong>User says:</strong> Typisch Starbucks, aber mit extremer Wartezeit und unfreundlicher Bedienung- aber wenn man seinen Kaffee morgens braucht kommt man wohl nicht drum herum..</p>
    #           <p><strong>Rating:</strong> 1</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>7 - Molto carino</h2>
    #           <p><strong>Published Date:</strong> 9/30/2020</p>
    #           <p><strong>User says:</strong> Locale molto carino e ordinato, ottimo per chi vuole spendere poco ma vuole una colazione o spuntino goloso. Comodissimo per il bicchiere di bevande da portare anche in giro.</p>
    #           <p><strong>Rating:</strong> 3</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>8 - Quick Coffee</h2>
    #           <p><strong>Published Date:</strong> 4/28/2020</p>
    #           <p><strong>User says:</strong> While on a city break in New York I stumbled across this Starbucks and made sure I went their every morning after that!

    # Staff are amazing and gave me a discount for being ex-military also a great vibe in there!

    # Favourite Starbucks in New York</p>
    #           <p><strong>Rating:</strong> 5</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div><div class="post">
    #           <h2>9 - vraiment pas top</h2>
    #           <p><strong>Published Date:</strong> 3/29/2020</p>
    #           <p><strong>User says:</strong> un starbuck minuscule dans lequel on est serrés comme des sardines pour boire un café à 4 dollars largement coupé à l'eau chaude plus que mauvais .Il y a des endroits bien plus sympas pour boire un café à New York (comme les Paris Baguette )</p>
    #           <p><strong>Rating:</strong> 1</p>
    #           <h3>Comments</h3>
    #           <input type="text" placeholder="Add a comment..." class="comment-input">
    #           <button class="post-comment">Post Comment</button>
    #       <div class="comments-list"></div></div></div>
    #     <div id="loading" style="display: none;">Loading...</div>

    #     <script src="script.js"></script>

    # <div aria-live="polite" id="bit-notification-bar" style="height: 42px; width: 100%; top: 0px; left: 0px; padding: 0px; position: fixed; z-index: 2147483647; visibility: visible;"><iframe style="height: 42px; width: 100%; border: 0px; min-height: initial;" id="bit-notification-bar-iframe" src="moz-extension://a931a247-baa3-4405-8d8d-a95a659c5dd2/notification/bar.html"></iframe></div></body></html>
