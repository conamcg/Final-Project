with open('eval_set.md', 'r') as f:
    content = f.read()

content = content.replace(
    '"I need my scheduling system access restored. I was out on\nleave for 3 weeks and my account appears to have been locked."',
    '"I was out on leave for 3 weeks and my account got locked. Can someone unlock it so I can log back in?"'
)
content = content.replace(
    '"Can someone add my new team member Sarah Johnson to the\nscheduling system? She starts Monday and will need standard\nscheduler access for the Memphis site."',
    '"Can someone set up a standard scheduler account for my new team member Sarah Johnson? She starts Monday at the Memphis site and just needs basic access."'
)
content = content.replace(
    '"The scheduling system is running slowly on my computer\ntoday. Other applications seem fine. Can someone take a look?"',
    '"The scheduling system is loading slowly on my laptop today. I restarted and it is still slow. Other apps are fine. Can IT take a look at my machine?"'
)

with open('eval_set.md', 'w') as f:
    f.write(content)

print('Done')