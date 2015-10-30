#!/usr/bin/python

import sys
import argparse
import subprocess
import os

USERNAME = 'EricYim'
CREDENTIALS = ' -u ' + USERNAME + ':c5c8705800b0a17639a1ce5f26abd0ae9075aacd'
POST_FLAG = ' -d'
BASE_URI = ' https://api.github.com/repos/EricYim/github_api_testing'
PULL_REQUEST_ENDPOINT = '/pulls'

uri = BASE_URI + PULL_REQUEST_ENDPOINT

def create_pull_request(args):
    global uri
    global USERNAME
    global CREDENTIALS
    global POST_FLAG

    pull_request_title = args.title
    pull_request_head = args.head
    if not pull_request_head:
        pull_request_head = subprocess.check_output('git rev-parse --abbrev-ref HEAD', shell=True)[:-1]
    pull_request_head = USERNAME + ':' + pull_request_head
    pull_request_base = args.base
    pull_request_body = args.body

    pull_request_params = ' \'{"'
    if pull_request_body:
        pull_request_params += 'body":"{0}","'.format(pull_request_body)
    pull_request_params += 'title":"{0}","head":"{1}","base":"{2}"'.format(pull_request_title, pull_request_head, pull_request_base)
    pull_request_params += '}\''
    post_params = POST_FLAG + pull_request_params

    # print post_params
    # print 'curl' + CREDENTIALS + post_params + uri
    os.system('curl' + CREDENTIALS + post_params + uri)

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="pull request title")
    parser.add_argument("-s", "--head", help="source branch")
    parser.add_argument("base", help="destination branch")
    parser.add_argument("-b", "--body", help="pull request contents", default="")
    args = parser.parse_args()
    create_pull_request(args)

if __name__ == "__main__":
    main(sys.argv[1:])    
