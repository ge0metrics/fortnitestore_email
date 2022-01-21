from modules import get_shop,construct_images,send_email,cleanup

#get items and save pages
all_shop_items=get_shop.retrieve()
construct_images.save_pages(all_shop_items)

#send email containing shop pages
send_email.send_email()

#clean up
cleanup.clean("icons")
cleanup.clean("out")