class RecentCounter(object):

    # class init of an empty list
    def __init__(self):

        self.reqs = []


    # ping method, appends the request time t to the reqs list, then while the first element is smaller than 3000 - t (i.e outside of the 3s window) remove that element
    # retrun the length of the reqs list once all requests with a t not in the inclusive range have been removed
    def ping(self, t):

        self.reqs.append(t)

        while self.reqs[0] < t - 3000:
            self.reqs.pop(0)

        return(len(self.reqs))