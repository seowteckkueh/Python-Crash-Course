current_users=['apple','ben','cloe','dan','eric','francis']
new_users=['grace','hank','iris','apple','cloe']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("username exist, please create a new username.")
    else:
        print("username available.")
