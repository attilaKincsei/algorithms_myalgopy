
# Algorithmic thinking related ToDos

- Collect job interview questions from companies you want to work for
  - JetBrains, Wikipedia, Google, Amazon, Facebook
  - Look for job postings
  - Are they looking for q/Python/Rust developers?
  - Look for company related job interview questions: coding/systems design
    - Amazon: [My favorite coding question to give candidates](https://carloarg02.medium.com/my-favorite-coding-question-to-give-candidates-17ea4758880c)
- Algorithm theory: Knuth
- Cracking the coding interview
- Solving algorithm: LeetCode, HackerRank
- Collect algorithm related tricks:
  - Sliding Window
  - Islands (Matrix Traversal)
  - Two Pointers
  - Fast & Slow Pointers
  - Merge Intervals
  - Cyclic Sort
  - In-place Reversal of a LinkedList
  - Tree Breadth-First Search
  - Tree Depth First Search
  - Two Heaps
  - Subsets
  - Modified Binary Search
  - Bitwise XOR
  - Top ‘K’ Elements
  - K-way Merge
  - Topological Sort
  - Unbounded Knapsack
  - Fibonacci Numbers
  - Palindromic Subsequence
  - Longest Common Substring


## [Most important classes of algorithms](https://hbfs.wordpress.com/2008/12/23/the-10-classes-of-algorithms-every-programmer-must-know-about/)


The 10 (classes of) Algorithms Every Programmer Must Know About
In Tunnels of Doom!, I wrote that the disjoint sets algorithm is one of the very few algorithms every programmer should know. That got me thinking. Should? What about must? If everyone must know about disjoint sets, what other algorithms must every programmer know about?

I made a “top ten” list of algorithms and data structures every programmer must know about.


The list would be as follows:

Lists, Arrays, Stack. Lists, arrays, and stacks are certainly the most basic data structures, yet, these building blocks can reserve a few surprises. For example, counter-intuitive sentinel nodes are extensively used in the STL to represent the position just passed the last element in a list. This makes, for example, the insertion of an item in the end() position rather efficient. While lists do not allow direct access to an element, arrays do, but at the cost of allocating a known a priori amount of memory. Conversely, inserting an element into a list, given the current position, is constant time, while to insert a new element in an array is more costly, depending on whether or not one wants to preserve ordering. Stacks are a special case of both, one could say, because they behave mostly like lists where operations are allowed only at one end; and like arrays because they are most often implemented in a contiguous span of memory, i.e., an array. As these three are common building blocks of more complex algorithms and data structures, you should really master them.
Trees. Trees, or more exactly search trees whether they be binary, k-ary, splay, AVL or B, are the next data structures on the list, offering O(\log n) operations for searching, inserting, and removing values (in the average case). The most interesting tree varieties try to insure that they also have worse cases in O(\log n), that is, they don’t go overly deep or take inordinately long to perform their operations. To do so, the prevailing strategy is to balance the tree so that it is of (almost) equal depth everywhere. Some varieties make the tree even shallower by having a branching factor much higher than two, like it is the case with (a,b) trees (also known sometimes as (n,m) trees). Splay trees, on the other hand, unbalances the trees to shift the most oft-accessed item near the root of the tree, while remaining a search tree.
Understanding these data structures and what trade-offs are involved will help you choose wisely which will suit your application better. Note that the structures that equalize depth do not only make sure that the worst case is the average case: they implicitly suppose that all items in the collection have an equal probability of being accessed—something quite contrary to the Pareto Principle (or more accurately, maybe, to Zipf’s law).

Sorting and Searching. Data does not always come in the right order, so it is possible that you will have to sort before applying any meaningful algorithm to it. Sorting is a complex topic, but I think that the two algorithms you really should know about are QuickSort and Radix Sort.
QuickSort is a comparison-based sort, that is, elements are compared to each other to determine their relative order. Eventually, QuickSort makes enough comparisons (O(n \log n) for n items, on average, but has a worst case of O(n^2)—which can be avoided, but that’s another story for now) to eventually produce a sorted list of items. The theoretical lower bound for comparison-based sorts is O(n \log n) comparisons, so QuickSort is doing very well on average. The great simplicity of the algorithm makes it very interesting in a very wide range of cases.

Radix sort, on the other hand, an address transformation sort that sorts the items in linear time, that is, in O(n), making it much faster than QuickSort. It is much faster, but Radix Sort is much simpler when keys are numeric or of fixed width; dealing with variable length keys efficiently makes the algorithm slightly more complex. Read more on Radix Sort here and in this old DDJ article.

Searching on a sorted array can be performed using the basic binary search in O(\log n) time. Creating and searching efficient indexes will also play a major role in managing and searching large data sets.

Priority Queues. Sometimes you don’t really care if a data set is completely sorted or not. You just want to determine rapidly its maximum (or minimum) valued item and remove it from the set. Ideally, determining the maximum item should be an O(1) operation, adding and removing values a O(\log n) operation. Turns out that heaps as implementation of priority queues are pretty efficient. Not only do they have efficient algorithms, they can also be implemented into contiguous arrays, dispensing one from using a pointer-based data structure, saving potentially a lot of memory. There are a lot of application of heaps, which range from scheduling (determining who goes next) to cache management (removing the oldest items from the cache).
Pattern Matching and Parsing. Every single one of us had to write a parser or a filter of some sort. Whether it’s to find data in an insanely large log or to read a simple configuration file. Not always, but very often, the sanest way to go around it is to use regular expressions, either using a library, such as Boost‘s regex, or Python‘s re, or by implementing the regular expression algorithms yourself—which would make it the insane way, I guess. Understanding how they work will greatly help you process and filter insufficiently structured data. Don’t ask why Perl is so popular.
Hashing. Hash functions play a central role in cryptography, error detection, cache management, and efficient look-up. Despite the superficial differences—the applications—all hash functions are closely related; in fact, they differ more in quality than nature. A hash function takes a message and deterministically produces a signature that looks like a pseudo-random number, n bits long, usually with n rather large, say 128 or 256. The harder it is to correlate the hash value with the original data, the safer the hash function is. If it is really hard to find the original data given a hash value, the function can serve as a one way function and be used in cryptographic applications. If the hash function is just good enough, it can serve as an (most probably) unique identifier for data items, which in turn can be used for cache management or hash tables. In either case, you have to understand the mathematics of the probability of collisions (two or more items hashing to the same value) so you can assess what hashing scheme is sufficient for your application. Read about von Mises’ birthday paradox to understand how to compute the probability of collision.
Disjoint Sets. The Disjoint sets data structure is a helper structure that you will need in a wide variety of algorithms, whether graph algorithms or image processing. Disjoint sets serves to represent multiple sets within a single array, each item being the member of one of many sets. Considered like that, this sounds like a rather special case, but in fact, there are a number of applications, not all obvious. Connected components arise in graph algorithms are most efficiently represented using the disjoint set data structure. It can also serve to segment an image, a process also know as computing the connected components or labeling. What’s also very interesting about disjoint sets is just how incredibly efficient operation are: using path compression, operations can be performed in expected constant time!
The special case where there are only two possible sets reverts to a simple bitmap, a data structure that is simple to manage and requires comparatively little memory—use of which can be further reduced, with a price, using Bloom filters.

Graph Algorithms and Data Structures. Problems like computing the minimum spanning tree, the determination of the shortest path between two nodes, matching, and the detection of cut vertexes will arise in a number of situation. Google’s PageRank, for example, is a very concrete application of graph algorithms. Often, seemingly unrelated problems can be mapped to graph algorithms for which very efficient algorithms, possibly dynamic programming related, already exist. There is also a large body of literature devoted to the data structures used for graphs, considering every possible special case: sparse, dense, clique-rich, or small world networks, etc.
Dynamic Programming. Closely related to graph algorithms, dynamic programming exploit the fact that the optimal solution to a large problem can be expressed as an optimal combination of sub-problems. Not all problems are amenable to this method, because not every objective function abide to the principle of optimality, but many optimization problems do. Dynamic programming exchanges memory for computation, a generally beneficent trade-off.
Memoization could be considered a limited form of dynamic programming where previous evaluations of an expensive function are cached and reused rather than recomputed if asked for again. Memoization greatly reduce computational complexity when used in combination with an optimization (or simply recursive) algorithm. For example, the n-th Fibonacci number can be computed in O(n) time using memoization, while the basic recursive formulation results in no less than O(F_n) \sim \phi^n calls! Here, \phi is Phidias‘s number, the golden ratio.

State Space Search Algorithms. Sometimes the scale of the problem, or the vastness of the state space makes it impossible to represent the problem as a graph. Consider chess as the example par excellence. The exact number of distinct valid states of the game is still debated, but is thought to be in the order of 10^{43}, and the number of arcs in the game graph somewhere around 10^{120}, as computed Shannon, therefore known as Shannon’s Number. It would be infeasible to search the graph corresponding to all possible games to determine the optimal move given any valid chess position. To deal with this immense state space, one would use one of the many state space search algorithms such as limited depth search, Breadth-first search, or if enough is known about the objective function, an algorithm like A*.
State space search is very often used for game artificial intelligence and other optimization problem where the structure is too complex, state space too vast, or of which too little is known to derive a more efficient algorithm.

Genetic algorithms are closely related to stochastic optimisation, where the state space is searched at many different points in parallel. The darwinist metaphor is apt, to a certain point, as “genes” (vectors) are “mutated” (varied randomly) to search the state space. Only the fittest (higher valued vectors, under the objective function) are kept for the next “generation” (iteration) others “die off” (are dropped).

I could have made the list much longer, at least to include topics such as data compression, a personal favorite. I could have included something about, say, control theory, which is also highly useful in the context of industrial informatics, but I also wanted the list to be a Ten Commandments type list (without the guilt and the vengeful God thing), something that would be easy to remember and that would apply to most programmers out there. Of course, you just read those and are thinking “why didn’t talked of XYZ”. Maybe I did miss something important; it may also be that “XYZ” is more of a niche topic than you think. I cannot think of this list as authoritative in any way; yet, it follows more or less closely what you will find a typical “Introduction to Algorithms” book. Either way, let met know.

This post is also in line with the “right toolbox” answer to one of Gnuvince’s commentator. I think that, again, it is not about being a guru in every of the ten topics I presented, but merely proficient, and to develop the reflex to see the similitudes between your current problem and one of the algorithms you already know, even though the mapping may not be exactly self-evident. This is not a “pick n out of m” list however. The more, the better. Make n=m.