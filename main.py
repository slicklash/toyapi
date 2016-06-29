#!/usr/bin/env python3

from argparse import ArgumentParser
from toyapi import Api

api = Api()
route = api.route
response = api.response


def main():

    arg_parser = ArgumentParser()
    arg_parser.add_argument('-b', '--bind', help='bind address', default='')
    arg_parser.add_argument('-p', '--port', help='port number', type=int, default=8081)
    arg_parser.add_argument('-d', '--dir', help='store dir')

    kwargs = vars(arg_parser.parse_args())

    api.register(ItemsResource())
    api.run(**kwargs)


class ItemsResource:

    def __init__(self):
        self.items = []

    @route('/items', 'GET')
    def query_items(self, request):
        return response(self.items)

    @route('/items', 'POST')
    def add_item(self, request):
        item = request.content
        if item:
            self.items.append(item)
        return response()

if __name__ == '__main__':
    main()
