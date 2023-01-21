# 0x00-pagination
In this project, I learned about pagination:
+ How to paginate a dataset with simple page and page_size parameters
+ How to paginate a dataset with hypermedia metadata
+ How to paginate in a deletion-resilient manner

---

+ [0. Simple helper function](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x00-pagination/0-simple_helper_function.py):
  - a function that returns the starting and ending page number as a tuple.
+ [1. Simple pagination](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x00-pagination/1-simple_pagination.py):
  - Server class to paginate a database of popular baby names. Implemented a method named ```get_page``` that returns the content of a particular page.
+ [2. Hypermedia pagination](https://github.com/Yosef-S-A/alx-backend-python/tree/main/0x00-pagination/2-hypermedia_pagination.py):
  - Implemented a ```get_hyper``` method for Server class. The method returns a dictionary with key-value pair describing page stats.
+ [3. Deletion-resilient hypermedia pagination](https://github.com/Yosef-S-A/alx-backend-python/tree/main/3-hypermedia_del_pagination.py):
  - Implemented a ```get_hyper_index``` method for Server class. The method returns a dictionary with the following key-value pairs:
    - index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index would be 60.
    - next_index: the next index to query with.
    - page_size: the current page size
    - data: the actual page of the dataset
