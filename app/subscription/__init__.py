#! /usr/bin/env python
# encoding:utf8
# vim: set ts=4 et sw=4 sts=4

"""
File: __init__.py
Author: "shanzi"
Email: "shanzi@diumoo.net"
Created At: 2013-06-07 23:39
Description: fetch, parse and storage feeds
"""


class SubscriptionHandler(object):
    """uses gevent to fetch, parse and handle a feedsource"""

    def __init__(self,url):
        """init with a url of subscription, this url must be a valid
        rss or atom feed url. you can retrieve the url from a general
        homepage with retrieve_feed_url in utils module
        """
        super(SubscriptionHandler ,self).__init__()
        self._get_or_create(url)

    def _get_or_create(self, url):
        """given a subscription entity of mongodb retrive data 
        from database and update the corresponding property of
        this instance. if such an subscription is not exists
        create one and assign default value for properties needed

        :url: @todo
        :returns: @todo

        """
        pass

    def update(self):
        """update the subscription source and do some statistics
        to decide proper interval of each update for the subscription
        source. return the statistic result
        
        :returns: None
        """
        # TODO: implement this function
        pass

    def proper_interval(self):
        """
        this function calculate proper interval to update this subscription
        
        :returns: a integer value in seconds
        """
        # TODO: implement this function
        pass

    def save(self):
        """save changes of the subscription into database
        :returns: @todo

        """
        # TODO: implement this function
        pass

class SubscriptionCenter(object):
    """arrange feed handling tasks such as create and update,
       distribute the tasks to SubscriptionHandler and handling
       scheduled update tasks
    """

    def __init__(self,db,base_interval=300):
        """init with db instance of mongodb"""
        super(SubscriptionCenter,self).__init__()
        self._db = db
        self._subscriptions = self._db.subscriptions
        self.ensure_index()
        self.BASE_INTERVAL = base_interval

    def ensure_index(self):
        """ensure the some index of collection subscriptions exists
        this function is auto called every time a feedCenter is inited

        :returns: None

        """
        # TODO: write the practical ensure index code
        self._subscriptions.ensure_index()

    def get_or_create_subscription(self, url):
        """given a subscription url of rss or atom,
        and create a new subscription entity and save it
        into mongodb or get the subscription from databse
        if there already exists a subscription entity with
        the same url

        :url: the url of subscription source(rss or atom)
        :returns: an instance of SubscriptionHandler
        """
        # TODO: implement this function 

    def update_subscription(self, url):
        """given a url to update, this function create a 
        SubscriptionHandler instance to handle update task
        if the subscription source of the specified url exists
        or it will throw an SubscriptionSourceNotFoundError

        :url: the url of subscription source to update
        :returns: None
        """
        # TODO: implement this function
        pass

    def tick(self):
        """this function is called every a few minutes
        (specified by base_interval property) to arrange and
        excute tasks such as update_subscription.
        :returns: None

        """
        # TODO: implement this function
        pass
        
def main():
    pass

if __name__=="__main__":
    main()
