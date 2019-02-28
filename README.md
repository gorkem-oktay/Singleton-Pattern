# Singleton Pattern

### About
In these repositories, some design patterns are implemented to a mini game system for self education. They may not be suited to use in an actual game (directly anyway). However, it is good to have some examples underhand to take reference. And even if anyone wants to use them, you are welcome.

### Definition
**_Singleton pattern_**, ensures a class has only one instance, and provides a global point of access to it.

### Description
Let's give a name to our character. But we should store it somewhere for later use, and the storage may be accessed from anywhere in the project. Also there should be just one of it. If we create it everytime, we will lose previous states and data stored in it. 

So we should keep an instance and don't let anyone recreating it or a new one. We can make its contructor private. Good, now nobody except itself can create it. But nobody except itself can create it. So we need to add a static (class) method to access that instance and if it is not initialized before we need to initialize it just for the first time. And that's all. Our storage becomes singleton.

It's very easy to implement and use singleton, it is composed of just one class anyway. However, we need to be careful about the implementation. Most applications are using multithreading (we should assume all of it uses). It means our only one singleton instance against many threads and it may cause inconsistent states and data. So to protect it, we should implement some checks or syncronizations, but again while doing it we should consider performance issues, especially with syncronizations.

Another side effect is, it also makes more difficult to unit test. As its motto says, there will be only one instance of it. On the other hand, there will be lots of tests and we can't create an instance for each test.
