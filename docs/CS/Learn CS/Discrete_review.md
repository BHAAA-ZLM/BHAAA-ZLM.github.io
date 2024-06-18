# Discrete Mathematics 2024 Finals Review

Lumi 

12112618

## Logic and Mathematical Proofs

**Proposition**: declarative sentence that is either true or false, but not both.

**Tautology**: A compound proposition that is always true, regardless of the truth values of the variables involved.

**Contradiction**: a compound proposition that is always false.

**Logical Equivalence**: denoted by $p \equiv q$, if $p \leftrightarrow q$ is a tautology. $p$ and $q$ always have the same truth value.
Logically equivalent propositions can be determined with truth tables or logical equivalences.

| Equivalence | Name | 
| --- | --- |
| $p \land T \equiv p$ $\\$ $p \lor F \equiv p$| Identity Law |
| $p \lor T \equiv T$ $\\$ $p \land F \equiv F$ | Domination Law |
| $p \lor p \equiv p$ $\\$ $p \land p \equiv p$ | Idempotent Law |
| $\neg(\neg p) \equiv p$ | Double Negation Law |
| $p \lor q \equiv q \lor p$ $\\$ $p \land q \equiv q \land p$ | Commutative Law |
| $(p \lor q) \lor r \equiv p \lor (q \lor r)$ $\\$ $(p \land q) \land r \equiv p \land (q \land r)$ | Associative Law |
| $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ $\\$ $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ | Distributive Law |
| $\neg(p \land q) \equiv \neg p \lor \neg q$ $\\$ $\neg(p \lor q) \equiv \neg p \land \neg q$ | De Morgan's Law |
| $p \lor (p \land q) \equiv p$ $\\$ $p \land (p \lor q) \equiv p$ | Absorption Law |
| $p \lor \neg p \equiv T$ $\\$ $p \land \neg p \equiv F$ | Negation Law |
| $p \rightarrow q \equiv \neg p \lor q$ | Implication Law |
| $p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$ | Equivalence Law |

**Predicate Logic**: make statements about variables that can be either true or false.

**Quantifiers**: $\forall$ (for all) and $\exists$ (there exists).
Quantifiers can exchange positions if they are of the same type and influencing the same domain.

**Validity**:
An argument form with premises $p_1, p_2, ..., p_n$ and conclusion $c$ is valid if and only if the compound proposition $(p_1 \land p_2 \land ... \land p_n) \rightarrow c$ is a tautology.

**Rules of Inference**:

| Rule | Tautology | Name |
| --- | --- | --- |
| \(\begin{array}{ll} & p \rightarrow q \\ & p \\ \hline \therefore & q \\ \end{array}\) | \((p \land (p \rightarrow q)) \rightarrow q\) | Modus Ponens |
| \(\begin{array}{ll} & p \rightarrow  q \\ & \neg q \\ \hline \therefore & \neg p \\ \end{array}\) | \((\neg q \land (p \rightarrow q)) \rightarrow \neg p\) | Modus Tollens |
| \(\begin{array}{ll} & p \rightarrow q \\ & q \rightarrow r \\ \hline \therefore & p \rightarrow r \\ \end{array}\) | \(((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)\) | Hypothetical Syllogism |
| \(\begin{array}{ll} & p \lor q \\ & \neg p \\ \hline \therefore & q \\ \end{array}\) | \(((p \lor q) \land \neg p) \rightarrow q\) | Disjunctive Syllogism |
| \(\begin{array}{ll} & p \\ \hline \therefore & p \lor q \\ \end{array}\) | \(p \rightarrow (p \lor q)\) | Addition |
| \(\begin{array}{ll} & p \land q \\ \hline \therefore & p \\ \end{array}\) | \((p \land q) \rightarrow p\) | Simplification |
| \(\begin{array}{ll} & p \\ & q \\ \hline \therefore & p \land q \\ \end{array}\) | \((p \land q) \rightarrow (p \land q)\) | Conjunction |

**Methods of Proving Theorems**:
1. Direct proof: Prove $p \rightarrow q$ directly.
2. Proof by contrapositive: Prove $\neg q \rightarrow \neg p$.
3. Proof by contradiction: Assume $\neg q \land p$ are true, and show that this leads to a contradiction.
4. Proof by cases: Prove $p \rightarrow q$ by dividing $p$ into cases, show it's true for all possible cases.
5. Proof of equivalence: Prove $p \leftrightarrow q$ by proving $p \rightarrow q$ and $q \rightarrow p$.

Examples:

Prove that $\sqrt{2}$ is irrational.
> Hint: proof by contradiction, setting $\sqrt{2} = \frac{a}{b}$, where $a$ and $b$ are coprime integers.

Prove that there are infinitely many prime numbers.
> Hint: proof by contradiction. Set $p_n$ as largest prime number, and consider $\Pi_{i=1}^n p_i + 1$.

Show that there exist irrational numbers $x$ and $y$such that $x^y$ is rational.
> Hint: consider $\sqrt{2}^{\sqrt{2}}$. Proof by cases.

## Set and Functions

A set is an unordered collection of objects. 

Proof of subset:
Show $A \subseteq B$ by showing $x \in A \rightarrow x \in B$.

**Cardinality**:
If there are exactly $n$ distinct elements in $S$, where $n$ is a non-negative integer, then $S$ is a finite set and $n$ is the cardinality of $S$, denoted by $|S| = n$.

**Power Set**:
The power set of a set $S$ is the set of all subsets of $S$, denoted by $\mathcal{P}(S)$.

**Tuples**:
The ordered n-tuple $(a_1, a_2, ..., a_n)$ is the ordered collection. 
Different from sets, the order of elements in a tuple matters.

**Cartesian Product**:
The Cartesian product of sets $A$ and $B$, denoted by $A \times B$, is the set of all ordered pairs $(a, b)$ where $a \in A$ and $b \in B$.

$$ A \times B = \{(a,b) | a \in A \land b \in B \} $$

**Union**: 
The union of sets $A$ and $B$, denoted by $A \cup B$, is the set of all elements that are in $A$ or in $B$.

$$ A \cup B = \{x | x \in A \lor x \in B\} $$

**Intersection**:
The intersection of sets $A$ and $B$, denoted by $A \cap B$, is the set of all elements that are in both $A$ and $B$.

$$ A \cap B = \{x | x \in A \land x \in B\} $$

**Difference**:
The difference of sets $A$ and $B$, denoted by $A - B$, is the set of all elements that are in $A$ but not in $B$.

$$ A - B = \{x | x \in A \land x \notin B\} $$

**Complement**:
The complement of set $A$ with respect to the universal set $U$, denoted by $\bar A$, is the set of all elements in $U$ that are not in $A$.

$$ \bar A = \{x | x \in U \land x \notin A\} $$

Principle of Inclusion-Exclusion:

$$ |A \cup B| = |A| + |B| - |A \cap B| $$

Set Identity Laws:

| Law | Name |
| --- | --- |
| $A \cup \emptyset = A$ $\\$ $A \cap U = A$ | Identity Law |
| $A \cup U = U$ $\\$ $A \cap \emptyset = \emptyset$ | Domination Law |
| $A \cup A = A$ $\\$ $A \cap A = A$ | Idempotent Law |
| $\bar{\bar A} = A$ | Double Complement Law |
| $A \cup B = B \cup A$ $\\$ $A \cap B = B \cap A$ | Commutative Law |
| $(A \cup B) \cup C = A \cup (B \cup C)$ $\\$ $(A \cap B) \cap C = A \cap (B \cap C)$ | Associative Law |
| $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ $\\$ $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ | Distributive Law |
| $A \cup \bar A = U$ $\\$ $A \cap \bar A = \emptyset$ | Complement Law |
| $A \cup (A \cap B) = A$ $\\$ $A \cap (A \cup B) = A$ | Absorption Law |
| $A \cup (B - A) = A \cup B$ $\\$ $A \cap (B - A) = \emptyset$ | Difference Law |
| $\bar{A \cup B} = \bar A \cap \bar B$ $\\$ $\bar{A \cap B} = \bar A \cup \bar B$ | De Morgan's Law |

**Proof of Set Identities**:
1. Using membership tables.
2. (e.g. $A=B$) By showing $A \subseteq B$ and $B \subseteq A$.
3. Use set builder and logical equivalences. 

Example for 3:
Prove that $\overline{A \cap B} = \bar A \cup \bar B$.

$$
\begin{align*}
    \overline{A \cap B} & = \{x | x \notin (A \cap B)\} \\
    & = \{x | \neg (x \in A \land x \in B)\} \\
    & = \{x | \neg x \in A \lor \neg x \in B\} \\
    & = \{x | x \notin A \lor x \notin B\} \\
    & = \{x | x \in \bar A \cup x \in \bar B\} \\
    & = \bar A \cup \bar B
\end{align*}
$$

**Functions**:
A function $f$ from set $A$ to set $B$ assigns to each element $a$ in $A$ exactly one element $b$ in $B$.

**Injective (One-to-One)**:
A function $f$ is injective if and only if for all $a_1, a_2 \in A$, $f(a_1) = f(a_2) \rightarrow a_1 = a_2$.

**Surjective (Onto)**:
A function $f$ is surjective if and only if for all $b \in B$, there exists an $a \in A$ such that $f(a) = b$.

**Bijective (One-to-One Correspondence)**:
A function $f$ is bijective if and only if it is both injective and surjective.

**Inverse Function**:
If $f$ is a bijective function from set $A$ to set $B$, then the inverse function of $f$, denoted by $f^{-1}$, is a function from $B$ to $A$ such that $f^{-1}(f(a)) = a$ for all $a \in A$ and $f(f^{-1}(b)) = b$ for all $b \in B$.

**Composition of Functions**:
The composition of functions $f: A \rightarrow B$ and $g: B \rightarrow C$ is the function $g \circ f: A \rightarrow C$ defined by $(g \circ f)(a) = g(f(a))$ for all $a \in A$.

**Sequences**:
A sequence is a function from a subset of the set of integers to a set $S$. 
Sequence can be defined recursively by providing one or more initial terms and a rule for determining subsequent terms from those that precede them.

### Cardinality of Sets

**Countable Sets**:
A set that is either finite or has the same cardinality as the set of positive integers is countable.

If there is a one-to-one function from set $A$ to set $B$, then $|A| \leq |B|$.

If there is a one-to-one correspondence between set $A$ and set $B$, then $|A| = |B|$.

If A and B are sets with $|A| \leq |B|$ and $|B| \leq |A|$, then $|A| = |B|$.

## Algorithm Complexity

**Big-O Notation**:
A function $f(n)$ is $O(g(n))$ if there exist constants $c$ and $n_0$ such that $|f(n)| \leq c|g(n)|$ for all $n \geq n_0$.

**Big-Omega Notation**:
A function $f(n)$ is $\Omega(g(n))$ if there exist constants $c$ and $n_0$ such that $|f(n)| \geq c|g(n)|$ for all $n \geq n_0$.

**Big-Theta Notation**:
A function $f(n)$ is $\Theta(g(n))$ if there exist constants $c_1$, $c_2$, and $n_0$ such that $c_1|g(n)| \leq |f(n)| \leq c_2|g(n)|$ for all $n \geq n_0$. 
In this case $f(n)$ is both $O(g(n))$ and $\Omega(g(n))$, $f(n)$ and $g(n)$ are of the same order.

## Number Theory

**Divisibility**:
An integer $a$ is divisible by an integer $b$ if there exists an integer $c$ such that $a = b \cdot c$.
If a, b, c are integers, where $a \not = 0$, such that $a | b$ and $a | c$, then $a | (mb + nc)$ whenever $m, n$ are integers.

### Congruence Relations
If $a, b$ are integers and $m$ is a positive integer, then $a$ is congruent to $b$ modulo $m$ if $m | (a - b)$, denoted by $a \equiv b \pmod{m}$.
$a$ and $b$ are congruent modulo $m$ if and only if there exists an integer $k$ such that $a = b + km$.

**Theorem**:
If $a \equiv b \pmod{m}$ and $c \equiv d \pmod{m}$, then:
1. $a + c \equiv b + d \pmod{m}$.
2. $ac \equiv bd \pmod{m}$.

**Corollary**:
Let $m$ be a positive integer and let $a$ and $b$ be integers. If $a \equiv b \pmod{m}$, then 
1. $(a + b) \pmod{m} = (a \pmod{m} + b \pmod{m}) \pmod{m}$.
2. $(a \cdot b) \pmod{m} = (a \pmod{m} \cdot b \pmod{m}) \pmod{m}$.

Computing $b^n \mod m$: 
1. Let $n = (a_{k-1} ... a_1 a_0)_2$.
2. Then $b^n = b^{(a_{k-1} ... a_1 a_0)_2} = b^{2^{k-1}a_{k-1}} \cdot ... \cdot b^{2a_1} \cdot b^{a_0}$.
3. Recall that $a \cdot b \pmod{m} = (a \pmod{m} \cdot b \pmod{m}) \pmod{m}$.
4. Successively find $b \mod m$, $b^2 \mod m$, $b^4 \mod m$, ... until $b^{2^{k-1}} \mod m$. Multiply the components of $b^{2^i}$ when $a_i = 1$.

Pseudo code for computing $b^n \mod m$:
```python
x = 1
power = b mod m
for i = 0 to k-1
    if a_i = 1
        x = (x * power) mod m
    power = (power * power) mod m
return x
```

If $ca \equiv cb \pmod{m}$, then $a \equiv b \pmod{m}$ only if $\gcd(a,b) = 1$. 

### Primes 

**Prime Numbers**:
An integer $p > 1$ is prime if its only positive divisors are 1 and $p$.

**Greatest Common Divisors**:
The greatest common divisor of integers $a$ and $b$, denoted by $\gcd(a,b)$, is the largest integer that divides both $a$ and $b$. If $a = p_1 ^{a_1} \cdot ... \cdot p_k ^{a_k}$ and $b = p_1 ^{b_1} \cdot ... \cdot p_k ^{b_k}$, then $\gcd(a,b) = p_1 ^{\min(a_1, b_1)} \cdot ... \cdot p_k ^{\min(a_k, b_k)}$.

**Relatively Prime**:
Integers $a$ and $b$ are relatively prime if $\gcd(a,b) = 1$.

**Least Common Multiple**:
The least common multiple of integers $a$ and $b$, denoted by $\text{lcm}(a,b)$, is the smallest positive integer that is divisible by both $a$ and $b$. If $a = p_1 ^{a_1} \cdot ... \cdot p_k ^{a_k}$ and $b = p_1 ^{b_1} \cdot ... \cdot p_k ^{b_k}$, then $\text{lcm}(a,b) = p_1 ^{\max(a_1, b_1)} \cdot ... \cdot p_k ^{\max(a_k, b_k)}$.

**Euclidean Algorithm**:
The Euclidean algorithm is an efficient method for computing the greatest common divisor of two integers $a$ and $b$.
1. If $a = 0$, then $\gcd(a,b) = b$.
2. If $b = 0$, then $\gcd(a,b) = a$.
3. Otherwise, apply the Euclidean algorithm to $b$ and $a \mod b$.

For example $\gcd(287, 91)$:

$$
\begin{align*}
    287 & = 3 \cdot 91 + 14 \\
    91 & = 6 \cdot 14 + 7 \\
    14 & = 2 \cdot 7 + 0
\end{align*}
$$


Lemma: Let $a = bq + r$. Then $\gcd(a,b) = \gcd(b,r)$.
Proof: Let $d = \gcd(a,b)$ and $d' = \gcd(b,r)$. Since $a = bq + r$, $d | a$ and $d | b$. Since $r = a - bq$, $d | r$. Thus $d | b$ and $d | r$, so $d | d'$. Similarly, $d' | b$ and $d' | r$, so $d' | a$. Since $a = bq + r$, $d' | a$. Thus $d' | d$, so $d = d'$
Another proof is also possible by showing all the common divisors of $a$ and $b$ are also common divisors of $b$ and $r$.

**Bezout's Theorem**:
If $a$ and $b$ are positive integers, then there exist integers $x$ and $y$ such that: 

$$ \gcd(a,b) = ax + by $$

This is also called the Bezout's Identity.

Can be found with the *extended Euclidean algorithm*.

Lemma: If $a | bc$ and $\gcd(a,b) = 1$, then $a | c$.
> Hint: Use Bezout's Theorem to express $c$ with $a$ and $b$.

Lemma: If $p$ is prime and $p | a_1 a_2 ... a_n$, then $p | a_i$ for some $i$.
> Hint: Use mathematical induction on $n$. Then prove by cases.

### Linear Congruences
A congruence of the form $ax \equiv b \pmod{m}$, where $m$ is a positive integer, $a$ and $b$ are integers, and $x$ is a variable, is called a linear congruence.

The solutions to a linear congruence $ax \equiv b \pmod{m}$ are all integers $x$ that satisfy the congruence. (More than 1 solution)

**Modular Inverse**:
An integer $a$ has a modular inverse modulo $m$ if there exists an integer $\bar{a}$ such that $\bar{a}a \equiv 1 \pmod{m}$.

We can solve the linear congruence $ax \equiv b \pmod{m}$ by finding the modular inverse of $a$ modulo $m$ and multiplying both sides by the modular inverse.

**When does the inverse exist?**
The modular inverse of $a$ modulo $m$ exists if and only if $a$ and $m$ are relatively prime. The inverse is unique modulo $m$.

**How do we find the inverse?**
With the *extended Euclidean algorithm*.

### Chinese Remainder Theorem

Let $m_1, m_2, ... m_n$ be pairwise relative prime positive integerse greater than 1 and $a_1, a_2, ..., a_n$ be arbitrary integers. Then the system:

$$
\begin{align*}
    x & \equiv a_1 \pmod{m_1} \\
    x & \equiv a_2 \pmod{m_2} \\
    & ... \\
    x & \equiv a_n \pmod{m_n}
\end{align*}
$$

has a unique solution modulo $m = \prod_{i=1}^n m_i$. The solution is given by:

$$ x = \sum_{i=1}^n a_i M_i \bar{M_i} \pmod{m} $$

where $M_i = \frac{m}{m_i}$ and $\bar{M_i}$ is the modular inverse of $M_i$ modulo $m_i$.

If $m_1, m_2, ... m_n$ are not pairwise relatively prime, then the system may have no solution or multiple solutions. But we can try to solve by translating the system into a system with pairwise relatively prime moduli. For $x \equiv a_k \pmod{m_k}$, suppose $m_k = p_1^{a_1} \cdot ... \cdot p_k^{a_k}$, where $p_i$ are all primes, then we can solve the system by solving $x \equiv a_k \pmod{p_i^{a_i}}$ for all $i$.

### RSA Cryptosystem
**Fermat's Little Theorem**:
If $p$ is a prime number and $a$ is an integer not divisible by $p$, then: 

$$ a^{p-1} \equiv 1 \pmod{p}$$

**RSA Cryptosystem**:
1. Choose two distinct prime numbers $p$ and $q$.
2. Compute $n = pq$ and $\phi(n) = (p-1)(q-1)$.
3. Choose an integer $e$ such that $1 < e < \phi(n)$ and $\gcd(e, \phi(n)) = 1$.
4. Compute the unique integer $d$ such that $1 \leq d < \phi(n)$ and $ed \equiv 1 \pmod{\phi(n)}$.
5. The public key is $(n,e)$ and the private key is $(n,d)$.
6. To encrypt a message $M$, compute $C = M^e \pmod{n}$.
7. To decrypt a ciphertext $C$, compute $M = C^d \pmod{n}$.

**Proof of RSA**: (Very short ver.)
1. $C^d = M^{ed} = M^{k\phi(n) + 1} = M \cdot (M^{\phi(n)})^k$.
2. By Fermat's Little Theorem, $M^{\phi(n)} \equiv 1 \pmod{n}$.
3. Thus $C^d \equiv M \pmod{n}$.

## Mathematical Induction

**Well Ordering Principle**:
Every nonempty set of nonnegative integers has a least element.

**Weak Principle of Mathematical Induction**:
1. Basic Step: Show that $P(0)$ is true.
2. Inductive Step: Show that for all $k \geq 0$, if $P(k)$ is true, then $P(k+1)$ is true.

**Strong Principle of Mathematical Induction**:
1. Basic Step: Show that $P(0)$ is true.
2. Inductive Step: Show that for all $k \geq 0$, if $P(0), P(1), ..., P(k)$ are true, then $P(k+1)$ is true.

## Recursion

To specify a function on the basis of recurrence:
1. Basis step (initial condition): specify the value of the function at $n = 0$ or other initial conditions.
2. Recursive step: specify a rule of finding the value of the function from its values at smaller arguments.

Finding the closed form of a recurrence relation:
1. Guess the form of the solution. (with Top-down or bottom-up approach)
2. Use mathematical induction to prove the correctness of the guess.

**Solving Linear Homogeneous Recurrence Relations**:

$$ a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k} $$

The characteristic equation is: 

$$ x^k - c_1 x^{k-1} - c_2 x^{k-2} - ... - c_k = 0 $$

Suppose these characteristic roots $\lambda_1, \lambda_2, ..., lambda_r$ have multiplicities $m_1, m_2, ... m_r$.
Then the general solution is:

$$ a_n = \sum_{i=1}^r \sum_{j=1}^{m_i} c_{ij} n^{j-1} \lambda_i^n $$

where $\lambda_i$ are the characteristic roots and $c_{ij}$ are constants determined by the initial conditions.

Find all the $c_{ij}$ with the initial conditions.

> _Example_:
$a_n = 4a_{n-1} - 4a_{n-2}$ with $a_0 = 1$ and $a_1 = 0$.
The characteristic equation is $x^2 - 4x + 4 = 0$, which has a double root $x = 2$.
Thus the general solution is $a_n = (c_1 + c_2 \cdot n )\cdot 2^n$.
Using the initial conditions, we find $c_1 = 1$ and $c_2 = -1$.
Thus the closed form is $a_n = 2^n - n \cdot 2^n$.

**Solving Linear Nonhomogeneous Recurrence Relations**:

$$ a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k} + f(n) $$

_Theorem_: 
If $a_n^{(p)}$ is a particular solution to the nonhomogeneous recurrence relation, and $a_n^{(h)}$ is the general solution to the corresponding homogeneous recurrence relation, then the general solution to the nonhomogeneous recurrence relation is $a_n = a_n^{(p)} + a_n^{(h)}$.
When $f(n)$ is a polynomial, try to find a particular solution of the form $a_n^{(p)} = q(n)$, where $q(n)$ is a polynomial with the same root of the same degree as $f(n)$. If the root is a solution to the characteristic equation, multiply by $n^m$ where $m$ is the multiplicity of the root in the characteristic equation.

> _Example_:
Find all solutions of the recurrence relation $a_n = 5a_{n-1} - 6a_{n-2} + 7^n$.
The characteristic equation is $x^2 - 5x + 6 = 0$, which has roots $x = 2, 3$.
The general solution to the homogeneous part is $a_n^{(h)} = c_1 \cdot 2^n + c_2 \cdot 3^n$.
Try a particular solution of the form $a_n^{(p)} = q(n) = A \cdot 7^n$.
Substitute into the recurrence relation to find $A = \frac{49}{20}$.
Thus the general solution is $a_n = c_1 \cdot 2^n + c_2 \cdot 3^n + \frac{49}{20} \cdot 7^n$.

## Counting

**Pigeonhole Principle**:
If $k$ objects are placed into $n$ boxes, then there is at least one box containing at least $\lceil \frac{k}{n} \rceil$ objects.

Example proofs:
Show that for every integer $n$, there is a multiple of n that has only 0s and 1s in its decimal expansion
> Hint: Consider the remainders of $1, 11, 111, ..., 111...1$ when divided by $n$.

During a month with 30 days, a baseball team plays at least one game a day, but no more than 45 games. Show that there must be a period of some number of consecutive days during which the team must play exactly 14 games.
> Hint: Number of games played before some day must be the same with another day + 14.

Every sequence of $n^2 + 1$ distinct real numbers contains a
subsequence of length $n + 1$ that is either strictly increasing or strictly decreasing.
> Hint: Consider the longest increasing and decreasing subsequence starting at $a_k$. If there is no subsequence of length $n+1$, then the two subsequences must have the same length starting at two different $a$. Show that this is impossible.

### Combinatorial proofs

A combinatorial proof of an identity is:
- a proof that uses counting arguments to prove that both sides of the identity count the same objects but in different ways.
- or a proof that is based on showing that there is a bijection between the sets of objects counted by the two sides of the identity.

Also called double counting proofs and bijective proofs (respectively).

**Binomial Theorem**:
For any positive integer $n$ and any real numbers $a$ and $b$, 

$$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

Corollary: 

$$\sum_{k=0}^n \binom{n}{k} = 2^n$$

Proved by simply replacing $a = b = 1$ in the binomial theorem.
Also can be proved by counting. Left side counts all subsets of a set with $n$ elements, right side counts the same thing since the object can either be in or out of the subset.

**Pascal's Identity**:
For any positive integers $n$ and $k$ with $n \geq k$, 

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

> Counting Proof: 
Left side counts all $k$-element subsets of a set with $n$ elements.
Right side counts the same thing by considering whether the $n$-th element is in the subset or not. If it's in the subset, then the remaining $k-1$ elements are chosen from the first $n-1$ elements. If it's not in the subset, then the $k$ elements are chosen from the first $n-1$ elements.

More Identities:

$$ \binom{n+1}{r + 1} = \sum_{j = r}^{n} \binom{j}{r} $$

> Direct proof: Can be proved using the Pascal's Identity.
Counting proof: Last place to find a final wanted item in a sequence of $n+1$ random items with $r + 1$ wanted items.

$$ \sum_{k = 1}^n k \binom{n}{k} = n \cdot 2^{n-1} $$

> Counting proof:
Left side counts the number of ways to choose a committee with a president from a group of $n$ people. 
Right side counts the same thing by first choosing the president and then choosing the rest of the committee.

**Vandermonde's Identity**:
For any nonnegative integers $m, n, r$,

$$\binom{m+n}{r} = \sum_{k=0}^r \binom{m}{k} \binom{n}{r-k}$$

**Combinations with Repetition**:
The number of ways to distribute $r$ objects to a set of $n$ objects with repetition allowed is $\binom{n+r-1}{r}$.

> Example: Number of ways to distribute 10 identical candies to 4 children.
Think of the candies as stars and the children as bars.

### Generating functions

The **generating function** for the sequence $a_0, a_1, a_2, ...$ is the infinite series

$$G(x) = a_0 + a_1 x + a_2 x^2 + ... + a_k x^k ... = \sum_{k=0}^\infty a_k x^k $$

We can transfer the problem of a combination problem into a probelm of finding coefficient of $x^r$ of a combination of generating function.

Common summation formula for generating functions:
1. $\frac{1 - x^{n+1}}{1 - x} = 1 + x + x^2 + ... + x^n= \sum_{k=0}^n x^k$
1. $(1-x)^{-1} = 1 + x + x^2 + ... = \sum_{k=0}^\infty x^k$
1. $(1-ax)^{-1} = 1 + ax + a^2x^2 + ... = \sum_{k=0}^\infty a^k x^k$
1. $(1-x)^{-2} = 1 + 2x + 3x^2 + ... = \sum_{k=0}^\infty (k+1)x^k$

Can be used to solve linear recurrence relations.

For example:
Consider the sequence $\{a_n\}$ that satisfies the recurrence relation 

$$ a_n = 8 a_{n-1} + 10^{n-1} $$ 

and the initial condition $a_1 = 9$.

Let $G(x) = \sum_{n = 0}^\infty a_n x^n$.
$a_0 = 1$ can be calculated with $a_1$.
Then the recurrence relation can be written as:

$$ 
\begin{align*}
    G(x) - a(0) & = \sum_{n = 1}^\infty a_n x^n = 8 \sum_{n = 1}^\infty a_{n-1} x^{n-1} + \sum_{n = 1}^\infty 10^{n-1} x^{n-1} \\
    & = 8x \sum_{n = 0}^\infty a_n x^n + \sum_{n = 0}^\infty 10^n x^n \\
    & = 8x G(x) + x /(1 - 10x) \\
    G(x) & = \frac{1-9x}{(1 - 8x)(1 - 10x)} \\
    & = \frac{1}{2}(\frac{1}{1 - 8x} + \frac{1}{1 - 10x}) \\
    & = \frac{1}{2}(\sum_{n = 0}^\infty 8^n x^n + \sum_{n = 0}^\infty 10^n x^n) \\
    & = \sum_{n = 0}^\infty \frac{8^n + 10^n}{2} x^n 
\end{align*}
$$

Therefore $a_n = \frac{8^n + 10^n}{2}$.

## Relations 

**Reflexive Relation**:
A relation $R$ on a set $A$ is reflexive if for all $a \in A$, $(a,a) \in R$.
Number of reflexive relations: $2^{n(n-1)}$.

**Irreflexive Relation**:
A relation $R$ on a set $A$ is irreflexive if for all $a \in A$, $(a,a) \notin R$.
Number of irreflexive relations: $2^{n(n-1)}$.

**Symmetric Relation**:
A relation $R$ on a set $A$ is symmetric if for all $a, b \in A$, $(a,b) \in R \rightarrow (b,a) \in R$.
Number of symmetric relations: $2^{n(n+1)/2}$.

**Antisymmetric Relation**:
A relation $R$ on a set $A$ is antisymmetric if for all $a, b \in A$, $(a,b) \in R \land (b,a) \in R \rightarrow a = b$.
Note that $(a,b) = (b,a)$ can happen in $R$ if they are both zeros.
Number of antisymmetric relations: $2^n \cdot 3^{n(n-1)/2}$.

**Transitive Relation**:
A relation $R$ on a set $A$ is transitive if for all $a, b, c \in A$, $(a,b) \in R \land (b,c) \in R \rightarrow (a,c) \in R$.

**Composite of Relations**:
The composite of relations $R$ and $S$, denoted by $R \circ S$, is the relation that consists of all pairs $(a,c)$ such that there exists an element $b$ in the domain of $S$ such that $(a,b) \in S$ and $(b,c) \in R$.

**Power of Relation**:
The $n$-th power of a relation $R$, denoted by $R^n$, is the relation defined inductively by:

$$ R^1 = R, R^{n+1} = R^n \circ R $$

Theorem: The relation $R$ on a set $A$ is transitive if and only if $R^n \subseteq R$.
> Hint: Just use the definitions.
Prove only if part with mathematical induction.

$R^n(i,j) = 1$ implies there is a path of length $n$ from $i$ to $j$ in the directed graph of $R$.

### Closure of Relations

**Closure**:
The closure of a relation $R$ on a set $A$ is the smallest relation $R'$ that contains $R$ with a certain property. 
By smallest, we mean that $R'$ is subset of every relation $Q$ that contains $R$ with the same property.

**Connectivity Relation**:
The connectivity relation $R^*$ on a set $A$ is the relation that contains all pairs $(a,b)$ such that there is a path from $a$ to $b$ in the directed graph of $R$.

$$ R^* = \bigcup_{n=1}^\infty R^n $$

Theorem: There is a path of length $n$ from $a$ to $b$ if and only if $(a,b) \in R^n$.
> Hint: Proved by induction.

Theorem: The transitive closure of a relation $R$ equals the connectivity relation $R^*$.
> Hint: Proved by showing that $R^*$ is transitive and contains $R$. Also that $R^*$ is the smallest transitive relation containing $R$. Since for all transitive relations $Q$, $Q^* \subseteq Q$ and $R^* \subseteq Q^*$.

**Finding the transitive closure of a relation**:

$$ R^* = R \cup R^2 \cup ... \cup R^n $$

Theorem: Let $M_R$ be the zero-one matrix of the relation $R$. Then the matrix of the transitive closure $R^*$ is 

$$ M_{R^*} = M_R \lor M_{R^2} \lor ... \lor M_{R^n}$$ 

**Roy-Warshall Algorithm**:

Consider a list of vertices $v_1, v_2, ... v_n$. Define a zero-one matrix 

$$ W_k = [w_{ij}^{(k)}] $$ 

where $w_{ij}^{(k)} = 1$ if there is a path from $v_i$ to $v_j$ that only uses vertices $v_1, v_2, ... v_k$.

To obtain the matrix $W_k$, we can use the formula:

$$ w_{ij}^{(k)} = w_{ij}^{(k-1)} \lor (w_{ik}^{(k-1)} \land w_{kj}^{(k-1)}) $$

```python
W = M_R
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            W[i,j] = W[i,j] or (W[i,k] and W[k,j])
```
The final matrix $W$ is the matrix of the transitive closure of $R$, $M_{R^*}$.

### Equivalence Relations

**Equivalence Relation**:
A relation $R$ on a set $A$ is an equivalence relation if it is reflexive, symmetric, and transitive.

**Equivalence Class**:
The equivalence class of an element $a$ in a set $A$ with respect to an equivalence relation $R$ is the set of all elements in $A$ that are related to $a$ by $R$.

$$ [a]_R = \{ x \in A | (a,x) \in R \} $$

**Partition**:
A partition of a set $A$ is a collection of nonempty subsets of $A$, i.e. $A_1, A_2, ... A_k$, such that:
1. $A_i \cap A_j = \emptyset$ for all $i \not = j$.
2. $ \bigcup_{i = 1}^k = A$.

Theorem: The equivalence classes of an equivalence relation on a set $A$ form a partition of $A$.

Theorem: Let $\{A_1, A_2, ..., A_n, ...\}$ be a partition of a set $A$. Then, there is an equivalence relation $R$ on $A$, that has the sets $A_i$ as its equivalence classes.

### Partial Ordering

**Partial Ordering**:
A relation $R$ on a set $A$ is a partial ordering if it is reflexive, antisymmetric, and transitive.

A set $S$ with a partial ordering $R$ is called a *partially ordered set* or *poset*, denoted by $(S,R)$.

Then notation $a \preccurlyeq b$ is used to denote that $(a,b) \in R$ in a poset $(S,R)$.

The notation $a \prec b$ denotes that $a \preccurlyeq b$ and $a \not = b$.

**Comparability**:

The elements $a$ and $b$ of a poset $(S,R)$ are comparable if either $a \preccurlyeq b$ or $b \preccurlyeq a$.

**Totally Ordered**:
A poset $(S,R)$ is totally ordered if for all $a, b \in S$, either $a \preccurlyeq b$ or $b \preccurlyeq a$. $\preccurlyeq$ is called a total order.


**Hasse Diagram**:
A Hasse diagram of a poset $(S,R)$ is a graph that represents the partial ordering $R$. By removing the edges that can be inferred from the transitive property of the relation, and all the loops.

**Lattice**:
A lattice is a poset $(S,R)$ such that for all $a, b \in S$, the set $\{a,b\}$ has both a least upper bound and a greatest lower bound.

**Topological Sorting**:
A topological sorting of a Hasse graph $G$ is an ordering of the vertices of $G$ such that for every set of vertices $(u,v)$, $u$ comes before $v$ in the ordering.

## Graph

### Undirected Graphs

**Simple Graph**:
A graph in which each edge connects two different vertices and where no two edges connect the same pair of vertices.

**Neighborhood**:
The set of all neighbors of a vertex $v$ in a graph $G$ is denoted by $N(v)$.

**Degree**:
The degree of a vertex $v$ in a graph $G$, denoted by $\deg(v)$, is the number of edges incident to $v$.

Handshaking Theorem:
If $G = (V,E)$ is an undirected graph with $m$ edges, then: 

$$ \sum_{v \in V} \deg(v) = 2m $$

**Connectivity**:
Two vertices $u$ and $v$ in a graph $G$ are connected if there is a path from $u$ to $v$.
The graph is *connected* if every pair of vertices is connected.

**Simple Path**:
A simple path in a graph $G$ is a path that does not contain any repeated vertices.

Lemma: If there is a path from $u$ to $v$ in a graph $G$, then there is a simple path from $u$ to $v$ in $G$.

**Cut vertices**:
A vertex $v$ in a connected graph $G$ is a cut vertex if the graph $G - v$ is disconnected.

**Cut edge**:
An edge $e$ in a connected graph $G$ is a cut edge if the graph $G - e$ is disconnected.

**Edge Connectivity**:
The edge connectivity of a graph $G$, denoted by $\lambda(G)$, is the minimum number of edges that must be removed to disconnect $G$.

**Euler Circuit**:
An Euler circuit in a graph $G$ is a circuit that contains every edge of $G$ exactly once.

**Euler Path**:
An Euler path in a graph $G$ is a path that contains every edge of $G$ exactly once.

Theorem:
A connected multigraph with at least two vertices has an Euler circuit if and only if every vertex has even degree.

Theorem 
A connected multigraph has an Euler path if and only if it has exactly two vertices of odd degree.

**Hamiltonian Circuit**:
A Hamiltonian circuit in a graph $G$ is a circuit that contains every vertex of $G$ exactly once.

**Hamiltonian Path**:
A Hamiltonian path in a graph $G$ is a path that contains every vertex of $G$ exactly once.

**Planar Graph**:
A graph is planar if it can be drawn in the plane without any edges crossing.

Theorem (Euler's Formula):
If $G$ is a connected planar graph with $v$ vertices, $e$ edges, and $r$ regions, then:

$$ r = e - v + 2 $$

> Proved by inductive hypothesis. Two cases: adding a vertex with edges, connecting two existing vertices.

Corollary: 
If $G$ is a connected planar graph with $v$ vertices and $e$ edges, where $v \geq 3$, then:

$$ e \leq 3v - 6 $$
 
> Hint: when $v \geq 3$, $\deg(r) \geq 3$. $2e = \sum_{r \in R} \deg(r) \geq 3r$.

If $G$ is a connected planar graph, then $G$ has a vertex of degree not exceeding 5.
> Show case is true with 1 or 2 vertices. Use the previous corollary to prove contradiction if every vertex has degree 6.

In a connected palnar simple graph with $v$ vertices and $e$ edges, where $v \geq 3$ and no circuits of length three, then:

$$ e \leq 2 v - 4 $$

> Similar to previous corollary, but with $\deg(r) \geq 4$.

**Kuratowski's Theorem**:
A graph is planar if and only if it does not contain a subgraph that is a subdivision of $K_5$ or $K_{3,3}$.

### Directed Graphs

The _in-degree_ of a vertex $v$ in a directed graph $G$, denoted by $\deg^-(v)$, is the number of edges that are incident to $v$. The _out-degree_ of a vertex $v$ in a directed graph $G$, denoted by $\deg^+(v)$, is the number of edges that are incident from $v$.

Let $G = (V,E)$ be a directed graph with $m$ edges. Then:

$$ \sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = m $$

**Strongly Connected**:
A directed graph $G$ is strongly connected if for every pair of vertices $u$ and $v$, there is a path from $u$ to $v$ and a path from $v$ to $u$.

**Weakly Connected**:
A directed graph $G$ is weakly connected if the underlying undirected graph is connected.

### Special Graphs: 
**Complete Graph**:
A complete graph on $n$ vertices, denoted by $K_n$, is a simple graph that contains an edge between every pair of distinct vertices.

**Cycle**:
A cycle of length $n$, denoted by $C_n$, is a simple graph that contains $n$ vertices and $n$ edges that form a cycle.

**$n$-dimensional Hypercube**:
The $n$-dimensional hypercube, denoted by $Q_n$, is a graph that has $2^n$ vertices, each of which is labeled with an $n$-bit string, and an edge between two vertices if their labels differ in exactly one bit.

### Bipartite Graphs

A graph $G = (V,E)$ is bipartite if the vertex set $V$ can be partitioned into two sets $V_1$ and $V_2$ such that every edge in $E$ connects a vertex in $V_1$ to a vertex in $V_2$.

**Complete Bipartite Graph**:
A complete bipartite graph $K_{m,n}$ is a bipartite graph that contains $m$ vertices in $V_1$ and $n$ vertices in $V_2$, and an edge between every pair of vertices in $V_1$ and $V_2$.

**Matching**:
A matching in a graph $G = (V,E)$ is a set of edges $M \subseteq E$ such that no two edges in $M$ share a vertex.

**Complete Matching**:
A complete matching in a graph $G$ with bipartition $(V_1, V_2)$, if every vertex in $V_1$ is incident to an edge in the matching, in this case $|M| = |V_1|$.
Matching is just a subset of all the edges.

**Hall's Marriage Theorem**:
Let $G = (V,E)$ be a bipartite graph with bipartition $(V_1, V_2)$. Then $G$ contains a complete matching from $V_1$ to $V_2$ if and only if for every subset $S \subseteq V_1$, $|N(S)| \geq |S|$.

> Proof of "only if" is easy, just consider the definition.
Proof of "if" is quite hard, can be proved with strong induction with proof by cases.
Suppose for $|V_1| = k$, the theorem holds for all $|\mathcal{P}(V_1)| < k$ such that $\forall A \in \mathcal{P}(V_1), |N(A)| \geq |A| \to$ Complete matching between $V_1$ and $V_2$.
Then consider the induction case with $|V_1| = k + 1$. Two cases could be discussed. One with all subsets having more neighbours, and one with some subsets having one-to-one matching.

**Isomorphic Graphs**:
Two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are isomorphic if there exists a bijection $f: V_1 \to V_2$ such that $(u,v) \in E_1$ if and only if $(f(u), f(v)) \in E_2$. Such a function $f$ is called an isomorphism.
Can be checked with:
1. Number of vertices and edges.
2. Degree of vertices.
3. Existence of circuits and paths with certain length etc.