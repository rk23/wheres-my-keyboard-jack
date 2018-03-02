import datetime
import praw

from decimal import Decimal

ORDER = <your order as an int, e.g. 100004345>
reddit = praw.Reddit()


def sort_by_timestamp(x):
    return x[2]


def append_order(comment):
    if "#1000" in comment.body:
        order_number = comment.body.split('#')[1] \
            .replace('?', ' ') \
            .replace('.', ' ') \
            .replace('(', ' ') \
            .replace('!', ' ') \
            .replace('\n', ' ') \
            .split(' ')[0]
        for reply in comment.replies.list():
            if '#' in reply.body:
                position = reply.body.split('#')[1] \
                    .split(' ')[0] \
                    .replace(',', '') \
                    .replace('!', '')
                timestamp = reply.created_utc
                orders.append((order_number, position, timestamp))


orders = []
week = datetime.datetime.now().strftime('%U')
for submission in reddit.subreddit('olkb').search(
        "Weekly Update & Question Thread for 2018-W{}".format(week)):
    if "Weekly Update & Question Thread" in submission.title:
        for comment in submission.comments.list():
            if type(comment) == praw.models.MoreComments:
                for more_comment in comment.comments():
                    append_order(more_comment)
            else:
                append_order(comment)

sorted_orders = sorted(orders, key=sort_by_timestamp, reverse=True)
order_position = ORDER - (int(sorted_orders[0][0]) - int(sorted_orders[0][1]))
most_recent_reply_timestamp = datetime.datetime.fromtimestamp(
    int(sorted_orders[0][2])).strftime('%B %d, %Y')

pessimistic_estimate = Decimal(order_position) / Decimal(50)
optimistic_estimate = Decimal(order_position) / Decimal(100)

print('As of {}, your order #{} has {} orders ahead of it.\n'
      'Optimistically it\'ll take {} weeks to ship your keyboard.\n'
      'Pessimistically it\'ll take {} weeks to ship your keyboard'.format(
          most_recent_reply_timestamp,
          ORDER,
          order_position,
          optimistic_estimate,
          pessimistic_estimate))
