#!/usr/bin/python
import ssl

import sys
import re
import urllib2


def get_url_with_protocol(url):
    pattern = re.compile("^https?://.*")
    if pattern.match(url):
        return url
    return "http://" + url


def get_resolved_url(url):
    try:
        response = urllib2.urlopen(url, context=ssl._create_unverified_context())
        return response.geturl()
    except urllib2.URLError, error:
        print error
        return


if __name__ == "__main__":
    if len(sys.argv) == 3:
        prefix = sys.argv[1]
        original = sys.argv[2]
        url = get_url_with_protocol(original)
        resolved = get_resolved_url(url)

        if resolved:
            print prefix + ": {\"original\": \"" + original + "\", \"resolved\": \"" + resolved \
                  + "\", \"reachable\": true}"
        else:
            print prefix + ": {\"original\": \"" + original + "\", \"resolved\": \"\", \"reachable\": false}"
    else:
        print "prefix, url or directory missing"
