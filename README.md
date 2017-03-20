# max-depth-crawler
Determines the no. of links that must be followed to reach a page starting from seed
page. Includeded a parameter that limits the depth of search. No pages whose depth
exceeds the depth parameter are included in the crawl.

e.g. if max value of depth parameter is zero the only page that must be crawled is
the seed page. If value of depth is 1, the pages that should be crawled must be seed
page and every page that is linked to it directly. If value of depth is 2, the crawl
should include all pages linked to these pages.
