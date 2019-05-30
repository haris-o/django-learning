django-learning

# TODO

* ~~App skeleton~~
* ~~Models~~
* ~~MUMA~~
* ~~Serializers~~
* ~~ViewSets~~
* ~~User authentication and authorization~~
* ~~Push code to VCS~~
* Testing
* Automated tests
* Celery


# Notes

### Choosing the base class to use

We have seen 4 ways to build API views until now

* Pure Django views
* APIView subclasses
* generics.* subclasses
* viewsets.ModelViewSet

So which one should you use when? My rule of thumb is,

* Use viewsets.ModelViewSet when you are going to allow all or most of CRUD operations on a model.
* Use generics.* when you only want to allow some operations on a model
* Use APIView when you want to completely customize the behaviour.