---
title: Learning Mathematical Logic
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 13min
publish_date: 2024.6.21
---

## Proposition and Connectives

**Proposition**: A proposition is a declarative sentence that can be judged as either true or false.

**Atomic Proposition**: A proposition that does not contain any smaller part that is still a proposition is called an atomic proposition.

**Compound Proposition**: A proposition that involves the assembly of multiple propositions is called a compound proposition.

## Formal Language

Formal language for propositional logic $\mathscr{L}^P$ is has three types of symbols:
1. Atomic propositions: $p, q, r, \ldots$
2. Connectives: $\neg, \land, \lor, \rightarrow, \leftrightarrow$
3. Parentheses: $(, )$

**Atom$(\mathscr{L}^P)$**: 
Set of expressions of $\mathscr{L}^P$ consisting of a proposition symbol only.

**Form$(\mathscr{L}^P)$**:
An expression $A \in \text{Form}\left(\mathscr{L}^P\right)$ if and only if it satisfies the following conditions:
1. $\text{Atom} (\mathscr{L}^P) \subseteq \text{Form} (\mathscr{L}^P)$
2. If $A \in \text{Form} (\mathscr{L}^P)$, then $\neg A \in \text{Form} (\mathscr{L}^P)$
3. If $A, B \in \text{Form} (\mathscr{L}^P)$, then $\left(A \land B\right), \left(A \lor B\right), \left(A \rightarrow B\right), \left(A \leftrightarrow B\right) \in \text{Form} (\mathscr{L}^P)$

**Sub formula**: A formula $A$ is a sub formula of a formula $B$ if $A$ is a part of $B$. $A$ is a proper sub formula of $B$ if $A$ is a sub formula of $B$ and $A \neq B$.

Lemma: Every well-formed formula of $\mathscr{L}^P$ has a unique parse tree.

Lemma: Every well-formed formula of $\mathscr{L}^P$ has an equal number of left and right parentheses.

Lemma: Every proper prefix of a well-formed formula of $\mathscr{L}^P$ has more left parentheses than right parentheses. Every proper suffix of a well-formed formula of $\mathscr{L}^P$ has more right parentheses than left parentheses.

**Precedence**:
1. $(, )$ has the highest precedence.
2. Precedence level: $\neg, \land, \lor, \rightarrow, \leftrightarrow$.
3. Connectives are assumed to associate to the right. e.g. $A \land B \land C$ is equivalent to $A \land (B \land C)$.


## Semantics
A truth valuation is a function $v : \text{Atom} (\mathscr{L}^P) \rightarrow \{0,1\}$.
For $p \in \text{Atom} (\mathscr{L}^P)$, $v(p)$ or $p^v$ is the truth value of $p$ under valuation $v$.

Every form $A \in \text{Form} (\mathscr{L}^P)$ has a truth value under a valuation $v$. 
> Proved by induction on the structure of $A$.

If for every valuation $v$, $A^v = 1$, then $A$ is said to be a **tautology**.
If for every valuation $v$, $A^v = 0$, then $A$ is said to be a **contradiction**.
If for some valuation $v$, $A^v = 1$, then $A$ is said to be **satisfiable**.

Semantics can be proved by:
1. Truth tables
2. Inductive proof
3. Valuation tree

**Logical equivalence**: 
Two formulas $A$ and $B$ are said to be logically equivalent if for every valuation $v$, $A^v = B^v$.  
$A$ and $B$ have same truth values in a truth table.
$A \leftrightarrow B$ is a tautology.

## Semantic Entailment

Let $\Sigma$ by a set of formulas ($\Sigma \subseteq \text{Form}(\mathscr{L}^P)$) and $A$ be a formula ($A \in \text{Form}(\mathscr{L}^P)$). We say:
- $A$ is a logical consequence of $\Sigma$, or
- $\Sigma$ (semantically) entails $A$, or
- $\Sigma \models A$
if and onlyl if for every valuation $v$, if $\Sigma^v = 1$ implies $A^v = 1$.

If $\Sigma \not \models A$, then there exists a truth valuation $v$ such that $\Sigma^v = 1$ and $A^v = 0$.

Proved using direct proofs or truth tables, or by contradiction.

$A \models B$ if and only if $A \to B$ is a tautology.
$A \equiv B$ if and only if $A \models B$ and $B \models A$.
$\varnothing \models A$  if and only if $A$ is a tautology.

$A_1, A_2, \ldots, A_n \models B$ if and only if $\varnothing \models (A_1 \land A_2 \land \ldots \land A_n) \to B$.

For any $n \geq 1$, there are $2^{2^n}$ distinct truth functions of $n$ variables.
> $2^n$ different truth values, output of each can be either 0 or 1.

**Adequate Set**:
A set of connectives is said to be adequate if every well-formed formula can be expressed using only those connectives.

Each of the sets $\{\neg , \land\}, \{\neg, \lor\}, \{\neg, \rightarrow\}$ is an adequate set of connectives.

## Proof Systems

If there is a proof with premises $\Sigma$ and conclusion $A$, then we say that $A$ is a syntactic consequence of $\Sigma$.
Denoted by: $\Sigma \vdash A$.

3 types of proof systems:
1. Natural deduction: Few axioms and many rules.
2. Hilbert system: Many axioms and only one rule. 
3. Resolution: Used to prove contradictions.

### Natural Deduction

**Alphabet of ND**:

$$ \Sigma = \{(, ), \neg, \land, \lor, \to,\leftrightarrow, p, q, r, \dots\}$$

**Formulas of ND**:
1. Atomic formulas are formulas.
2. If $A$, $B$ are formulas, then $(\neg A)$, $(A \land B)$, $(A \lor B)$, $(A \to B)$, $(A \leftrightarrow B)$ are formulas.
3. Only expressions of $\Sigma$ that can be derived from the above rules are formulas.

#### Inference rules:

**Reflexivity (Premise)**: $ \Sigma \cup \{\alpha \} \vdash \alpha$.

A table of all inference rules:

| Name | $\vdash$ Notation | Inference Notation | 
|---|---|---|
| $\land$ - Introduction | if $\Sigma \vdash \alpha$ and $\Sigma \vdash \beta$, then $\Sigma \vdash (\alpha \land \beta)$. | $\begin{array}{c} \alpha \\ \beta \\ \hline (\alpha \land \beta) \end{array}$ |
| $\land$ - Elimination | if $\Sigma \vdash (\alpha \land \beta)$, then $\Sigma \vdash \alpha$ and $\Sigma \vdash \beta$. | $\begin{array}{c} (\alpha \land \beta) \\ \hline \alpha \end{array}$ and $\begin{array}{c} (\alpha \land \beta) \\ \hline \beta \end{array}$ |
| $\to$ - Elimination | if $\Sigma \vdash \alpha$ and $\Sigma \vdash (\alpha \to \beta)$, then $\Sigma \vdash \beta$. | $\begin{array}{c} \alpha \\ (\alpha \to \beta) \\ \hline \beta \end{array}$ |
| $\to$ - Introduction | if $\Sigma \cup \{\alpha\} \vdash \beta$, then $\Sigma \vdash (\alpha \to \beta)$. | $\begin{array}{c} \boxed{\begin{array}{c} \alpha \\ \vdots \\ \beta \end{array}} \\[8mm]  \hline \alpha \to \beta \end{array}$ |
| $\lor$ - Introduction | if $\Sigma \vdash \alpha$, then $\Sigma \vdash (\alpha \lor \beta)$ and $\Sigma \vdash (\beta \lor \alpha)$. | $\begin{array}{c} \alpha \\ \hline (\alpha \lor \beta) \end{array}$ and $\begin{array}{c} \alpha \\ \hline (\beta \lor \alpha) \end{array}$ |
| $\lor$ - Elimination | if $\Sigma \vdash (\alpha \lor \beta)$ and $\Sigma \cup \{\alpha\} \vdash \gamma$ and $\Sigma \cup \{\beta\} \vdash \gamma$, then $\Sigma \vdash \gamma$. | $\begin{array}{c} (\alpha \lor \beta) \\ \boxed{\begin{array}{c} \alpha \\ \vdots \\ \gamma \end{array}} \\[8mm] \boxed{\begin{array}{c} \beta \\ \vdots \\ \gamma \end{array}} \\[8mm] \hline \gamma \end{array}$ |
| $\neg$ - Introduction | if $\Sigma \cup \{\alpha\} \vdash \perp$, then $\Sigma \vdash \neg \alpha$. | $\begin{array}{c} \boxed{\begin{array}{c} \alpha \\ \vdots \\ \perp \end{array}} \\[8mm] \hline \neg \alpha \end{array}$ |
| $\perp$ - Introduction | if $\Sigma \vdash \neg \alpha$ and $\Sigma \vdash \alpha$, then $\Sigma \vdash \perp$. | $\begin{array}{c} \neg \alpha \\ \alpha \\ \hline \perp \end{array}$ |
| $\perp$ - Elimination | if $\Sigma \vdash \perp$, then $\Sigma \vdash \alpha$. | $\begin{array}{c} \perp \\ \hline \alpha \end{array}$ |
| $\neg \neg$ - Elimination | if $\Sigma \vdash \neg \neg \alpha$, then $\Sigma \vdash \alpha$. | $\begin{array}{c} \neg \neg \alpha \\ \hline \alpha \end{array}$ |

And the law of excluded middle: $\vdash (p \lor \neg p)$.

## Soundness and Completeness

$\Sigma \vdash A$ means that $A$ is a logical consequence (in the deduction system) of $\Sigma$.

$\Sigma \models A$ if and only if for every valuation $v$, if $\Sigma^v = 1$, then $A^v = 1$.

**Soundness**: If $\Sigma \vdash A$, then $\Sigma \models A$.
The conclusion of a proof is always a logical consequence of the premises.
> Proved by induction on the length of the proof.

**Completeness**: If $\Sigma \models A$, then $\Sigma \vdash A$.
Every logical consequence can be proved in this proof system.
> Quite difficult to prove.
> We want to prove: If $\Sigma \models A$ holds, then $\Sigma \vdash A$ is valid.
> We need to use three lemmas: 

> 1. **Lemma 1**: If $\Sigma \models A$, then $\varnothing \models (\alpha_0 \to (\alpha_1 \to (\dots \to (\alpha_n \to A)\dots )))$.
>> Proved by contradiction. Assuming $\varnothing \not \models (\alpha_0 \to (\alpha_1 \to (\dots \to (\alpha_n \to A)\dots )))$ and showing that $\Sigma \not \models A$.

> 2. **Lemma 2**: If $\varnothing \models A$, then $ \varnothing \vdash A$.
>> Proved by induction on the structure of $A$. Introduction of a new symbol $\hat p$ which is $\neg p$ when $p^v = 0$ and $p$ when $p^v = 1$.

> 3. **Lemma 3**: If $\varnothing \vdash (\alpha_0 \to (\alpha_1 \to (\dots \to (\alpha_n \to A)\dots )))$, then $\{\alpha_0, \alpha_1, \dots, \alpha_n\} \vdash A$. Which is equivalent to $\Sigma \vdash A$.
>> Direct proof (like pealing onions).

# First Order Logic

## Syntax

**Domain**: 
A non-empty set of objects.

**Constant symbols**: 
Constants are used to denote objects in the domain.

**Variables**: 
"Place holders" for concrete values.

**Predicate**: 
A predicate is a function that returns a truth value.
Representing the property of an individual object in the domain, or the relationship between multiple objects.

**Quantifiers**:

1. Universal quantifier: $\forall x$, statement is true for all $x$ in the domain.

2. Existential quantifier: $\exists x$, statement is true for at least one $x$ in the domain.

**Function symbols**:
Functions that take objects in the domain as input and return an object in the domain as output, denoted as $f^{(n)}(x)$.

**Terms**:
Is defined inductively as:

1. Constant symbols and variables are terms.

2. If $f^{(n)}$ is a function symbol of arity $n$, and $t_1, t_2, \ldots, t_n$ are terms, then $f^{(n)}(t_1, t_2, \ldots, t_n)$ is a term.

3. Nothing else is a term.

Intuitive understanding: Terms are expressions that denote objects in the domain.

**Atomic formula**:
An expression $\mathscr{L}$ is an element of $\text{Atom}(\mathscr{L})$ if and only if it has one of the following two forms:

1. $P(t_1, \dots, t_n)$, where $P$ is an $n$-ary predicate symbol and $t_1, \dots, t_n \in \text{Term}(\mathscr{L})$.

2. $t_1 = t_2$, where $t_1, t_2 \in \text{Term}(\mathscr{L})$.

Intuitive understanding: Atomic formulas are expressions that denote a truth value, indicating the properties or relations of objects.

**Formulas**:
$\alpha \in \text{Form}(\mathscr{L})$ if and only if it satisfies the following conditions:

1. $\text{Atom}(\mathscr{L}) \subseteq \text{Form}(\mathscr{L})$.

2. If $\alpha \in \text{Form}(\mathscr{L})$, then $\neg \alpha \in \text{Form}(\mathscr{L})$.

3. If $\alpha, \beta \in \text{Form}(\mathscr{L})$, then $\left(\alpha \land \beta\right), \left(\alpha \lor \beta\right), \left(\alpha \rightarrow \beta\right), \left(\alpha \leftrightarrow \beta\right) \in \text{Form}(\mathscr{L})$.

4. If $\alpha \in \text{Form}(\mathscr{L})$ and $x$ is a variable, then $\forall x \alpha, \exists x \alpha \in \text{Form}(\mathscr{L})$.

## Semantics

**Scope**:
The scope of a quantifier is the formula that follows it. e.g. In $\forall x P(x) \land Q(x)$, the scope of $\forall x$ is $P(x) \land Q(x)$.

**Free and bound variables**:
A variable $x$ is free in a formula $\alpha$ if it is not in the scope of any quantifier for $x$. Otherwise, it is bound.

**Sentence**:
A formula is a sentence if all its variables are bound.

**Closure**:
The closure of a formula $\alpha$ is the set of all sentences that can be formed by replacing the free variables in $\alpha$ with constants.
Universal closure of $\alpha$ is $\forall x_1 \forall x_2 \ldots \forall x_n \alpha$.
Existential closure of $\alpha$ is $\exists x_1 \exists x_2 \ldots \exists x_n \alpha$.

### Meanings
To assign meanings to formulas of FOL, we need:

- A domain $D$.

- An interpretation $I$ of non-logical symbols that assigns:
    - To each constant symbol $c$, an object $c^I \in D$.

    - To each function symbol $f^{(n)}$, a function $f^I : D^n \to D$.

    - To each predicate symbol $P^{(n)}$, a relation $P^I \subseteq D^n$.

- An interpretation of logical symbols:

    - Logical connectives, punctuations

    - Quantifiers, variable symbols...

After interpretation, terms in FOL represent individuals in the domain, while formulas represent propositions with fixed truth values.

**Interpretation**:
An interpretation $I$ consists of:

- A non-empty domain $D$.

- For each constant symbol $c$, an object $c^I \in D$.

- For each function symbol $f^{(n)}$, a function $f^I : D^n \to D$.

- For each predicate symbol $P^{(n)}$, a relation $P^I \subseteq D^n$.

**Environment**:
An environment $E$ is a function that assigns a value in the domain to every variable symbol in the language.

**Value of terms**:
With a fix interpretation $I$ and environment $E$, the value of a term $t$ is denoted as $t^{(I,E)}$, and is defined as:

- If $t$ is a constant symbol $c$, then $t^{(I,E)} = c^I$.

- If $t$ is a variable symbol $x$, then $t^{(I,E)} = E(x)$.

- If $t = f(t_1, t_2, \ldots, t_n)$, then $t^{(I,E)} = f^I(t_1^{(I,E)}, t_2^{(I,E)}, \ldots, t_n^{(I,E)})$.

**Value of atomic formulas**:  
With a fix interpretation $I$ and environment $E$, the value of an atomic formula $P(t_1, t_2, \ldots, t_n)$ is denoted as $P(t_1, t_2, \ldots, t_n)^{(I,E)}$, and has the truth value of $P^I(t_1^{(I,E)}, t_2^{(I,E)}, \ldots, t_n^{(I,E)})$.

**Value of Well-Formed Formulas**:
With a fix interpretation $I$ and environment $E$, the value of a well-formed formula $\alpha$ is denoted as $\alpha^{(I,E)}$, and is defined as:

- If $\alpha$ is an atomic formula, then $\alpha^{(I,E)} = P(t_1, t_2, \ldots, t_n)^{(I,E)}$.

- If $\alpha = \neg \beta$, then $\alpha^{(I,E)} = 1 - \beta^{(I,E)}$.

- If $\alpha = \beta \land \gamma$, then $\alpha^{(I,E)} = \beta^{(I,E)} \land \gamma^{(I,E)}$.

- If $\alpha = \beta \lor \gamma$, then $\alpha^{(I,E)} = \beta^{(I,E)} \lor \gamma^{(I,E)}$.

- If $\alpha = \beta \to \gamma$, then $\alpha^{(I,E)} = 1 - \beta^{(I,E)} \lor \gamma^{(I,E)}$.

- If $\alpha = \beta \leftrightarrow \gamma$, then $\alpha^{(I,E)} = \beta^{(I,E)} \leftrightarrow \gamma^{(I,E)}$.

- If $\alpha = \forall x \beta$, then $\alpha^{(I,E)} = 1$ if for all $d \in D$, $\beta^{(I, E[x \mapsto d])} = 1$.

- If $\alpha = \exists x \beta$, then $\alpha^{(I,E)} = 1$ if there exists $d \in D$ such that $\beta^{(I, E[x \mapsto d])} = 1$.

Assignment:
For any environment $E$ and domain element $d$, the new environment "$E$ with $x$ re-assigned to $d$" is denoted as $E[x \mapsto d]$., is given by:
$$E[x \mapsto d](y) = \begin{cases} d & \text{if } y = x \\ E(y) & \text{otherwise} \end{cases}$$

## Entailment

An interpretation $I$ and environment $E$ satisfies a formula $\alpha$ if and only if $\alpha^{(I,E)} = 1$, denoted as $I \models_E \alpha$. If they do not satisfy, then $I \not \models_E \alpha$, if $\alpha^{(I,E)} = 0$.
If $I \models_E \alpha$ for all environments $E$, then $I \models \alpha$.

A formula $\alpha$ is:

- valid if $I \models \alpha$ for all interpretations $I$ and $E$.

- satisfiable if $I \models \alpha$ for some interpretation $I$ and $E$.

- unsatisfiable if $I \not \models \alpha$ for all interpretations $I$ and $E$.

## Natural Deduction fo First Order Logic

**Substitutions**:
For a variable $x$, a term $t$, and a formula $\alpha$, the substitution of $t$ for $x$ in $\alpha$ is denoted as $\alpha[t/x]$ which denotes the resulting formula by replacing each free occurrence of $x$ in $\alpha$ with $t$.

Natural deduction rules for FOL:

| Name | $\vdash$ Notation | Inference Notation |
|---|---|---|
| $\forall$ - Elimination | if $\Sigma \vdash \forall x \alpha$, then $\Sigma \vdash \alpha[t/x]$ for any term $t$. | $\begin{array}{c} \forall x \alpha \\ \hline \alpha[t/x] \end{array}$ |
| $\forall$ - Introduction | if $\Sigma \vdash \alpha[t/x]$ with $t$ not free in $\Sigma$ or $\alpha$, then $\Sigma \vdash \forall x \alpha$. | $\begin{array}{c} \boxed{\begin{array}{c} t \text{ fresh}\  \\ \vdots \\ \alpha[t/x] \end{array}} \\[7mm] \hline \forall x \alpha \end{array}$ |
| $\exists$ - Introduction | if $\Sigma \vdash \alpha[t/x]$, then $\Sigma \vdash \exists x \alpha$. | $\begin{array}{c} \alpha[t/x] \\ \hline \exists x \alpha \end{array}$ |
| $\exists$ - Elimination | if $\Sigma \cup \{\alpha[t/x]\} \vdash \beta$ with $t$ fresh, then $\Sigma \cup (\exists x \alpha) \vdash \beta$. | $\begin{array}{c} \exists x \alpha \\ \boxed{\begin{array}{c} \alpha[t/x], t \text{ fresh} \\ \vdots \\ \beta \end{array}} \\[7mm] \hline \beta \end{array}$ |