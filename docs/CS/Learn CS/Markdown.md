---
tags:
    - Markdown

author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 25min
publish_date: 2022.7.18


---

<!-- # <span style="font-family: Courier">Learning Markdown -->

<span style="font-family: Courier"> 
Markdown is a kind of text file which can be converted to HTML with Markdown applications and Markdown. I find it very interesting and kinda cool to write things in this way.

---

## <span style="font-family: Courier">Basic Syntax

### <span style="font-family: Courier">**Headings**

```
Markdown                    HTML
# Heading level 1           <h1> Heading level 1</h1>
...                         ...
###### Heading level 6      <h6> Heading level 6</h6>
```
<span style="font-family: Courier"> or
```
Markdown                    HTML
Heading level 1             <h1> Heading level 1</h1>
===============

Heading level 2             <h2> Heading level 1</h2>
---------------             
```

### <span style="font-family: Courier">**Paragraphs**

<span style="font-family: Courier">
A blank line can create a paragraph betwen some lines.

```
Markdown
I really like using Markdown.

I think I'll use it from now on.
--------------------------------
HTML
<p>I really like using Markdown.</p>

<p>I think I'll use it from now on.</p>
```

### <span style="font-family: Courier">**Line Breaks**

<span style="font-family: Courier">
Create a line break with ending the first line with two or more spaces and press return.

```
Markdown
First Line  
Second Line

HTML
<p>First Line<br />
Second Line</p>
```

### <span style="font-family: Courier">**Bold**
```
Markdown
**bold text**
__bold text__

HTML 
<strong>bold text</strong>
```

### <span style="font-family: Courier">**Italics**
```
Markdown
*Italic text*
_Italic text_

HTML
<em>Italic text</em>
```

<span style="font-family: Courier">
Combine bold and italic syntax to create bold and italic text.

### <span style="font-family: Courier">**Blockquotes**

<span style="font-family: Courier">
Including multi-paragraphs, and blockquotes inside blockquotes. You can also add other markdown elements into blockquotes, but you'll need some experiments.

> <span style="font-family: Courier">This is a blockquote.
>
> <span style="font-family: Courier">This is second para.
>> <span style="font-family: Courier">This is nested blockquotes.

```
Mardown
>This is a blockquote.
>
>This is second para.
>>This is nested blockquotes.

HTML
<blockquote>
    <p>This is a blockquote.</p>
    <p>This is second para.</p>
    <blockquote>
        <p>This is nested blockquotes.</p>
    </blockquote>
</blockquote>
```

### <span style="font-family: Courier">**Lists**
#### <span style="font-family: Courier">**Ordered Lists**

<span style="font-family: Courier">
    <ol>
        <li><span style="font-family: Courier">This is an</span></li>
        <li><span style="font-family: Courier">ordered list.</span></li>
        <li><span style="font-family: Courier">In markdown the order of </span></li>
        <li><span style="font-family: Courier">the number in front doesn't matter.</span></li>
    </ol>
</span>



<span style="font-family: Courier">
There is a small bug, when you are trying to set the font for the text, the ordered list doesn't work very smoothly. The number's don't show as they shoul, nor does the hyperlinks.

1. <span style="font-family: Courier">You need to change the font
6. <span style="font-family: Courier">in the ordered list.

<span style="font-family: Courier">
Also, you can nest the list items by four spaces or a tab.

```
Markdown
1.First Item
1.Second Item
    3.A nesting orderded list.
    6.Like I said, numbers in front doesn't matter.
1.Third Item

HTML
<ol>
    <li>First Item</li>
    <li>Second Item</li>
        <ol>
            <li>A nesting orderded list.</li>
            <li>Like I said, numbers in front doesn't matter.</li>
        </ol>
    <li>Third Item</li>
</ol>
```

#### <span style="font-family: Courier">**Unordered Lists**

<span style="font-family: Courier">
Unordered lists can be created by 

- <span style="font-family: Courier">adding dashes (-), 
* <span style="font-family: Courier">asterisks(*), 
+ <span style="font-family: Courier">or plus signs(+) in front of the line items.

<span style="font-family: Courier">
The unordered list can also be nested by adding tabs in front of the list.

```
Markdown
- First Line
- Second Line
    - The Nested Line
- Third Line

HTML
<ul>
    <li>First Line</li>
    <li>Second Line</li>
        <ul>
            <li>The nested line</li>
        </ul>
    <li>Third Line
</ul>
```

#### <span style="font-family: Courier">**Adding Elements in Lists**

<span style="font-family: Courier">
You can add other elements to a list with an extra tab in front of the elements.

<span style="font-family: Courier">
e.g. two tabs in front of a code (code normally need one tab)

### <span style="font-family: Courier">**Code**

<span style="font-family: Courier">
When you want to denote a word or phrase as a code, enclose the phrase and code in `tick marks` (`).

```
Markdown
This is the word for `code`.

HTML
This is the word for <code>code</code>.
```

<span style="font-family: Courier">
You can also escape tick marks with double tick marks when your code contains tick marks.

```
``This is a code containing `tick marks`.``
```

<span style="font-family: Courier">
You can also write code blocks when you add tabs to every line.
    
    public static main void(String[] args){
        System.out.println("Hello world")
    }

    HTML
    <pre>
        <code>
            &lt;public static main void(String[] args){&gt;
                &lt;System.out.println("Hello world")&gt;
            &lt;}&gt;
        </code>
    </pre>

### <span style="font-family: Courier">**Horizontal Rules**

<span style="font-family: Courier">
Sometimes you want a horizontal line to seperate the contents you can add three

---
<span style="font-family: Courier">dashes(---)
***
<span style="font-family: Courier">asteriks(***)
___
<span style="font-family: Courier">underscores(___)

<span style="font-family: Courier">
to creat the horizontal line. Or in HTML fashion: `<hr />`
</span>

### <span style="font-family: Courier">**Links**

<span style="font-family: Courier">
You can add titles to your links by adding the title behind the link seperated by a space and surrounded by the quotation marks ("").

```
Markdown
Use [Duck Duck Go](https://duckduckgo.com "My favourite search engine")

HTML
<p> Use <a href="https://duckduckgo.com" title="My favourite search engine">Duck Duck Go</a>. </p>
```

<span style="font-family: Courier">
Also you can turn a URL or an email address into a link simply by enclosing it in angle brackes.

<12112618@mail.sustech.edu.cn>

    <12112618@mail.sustech.edu.cn>

<span style="font-family: Courier">
You can still format the links using the normal bold and italic format.

<span style="font-family: Courier">
You can also write **Reference-style Links**


<span style="font-family: Courier">
The first part of the reference-style link is the inline part, and is formatted with two sets of brackets.(You can add spaces between the two sets of brackets, but it's a bit wierd.)

[reference-style link][1]

[1]:<https://google.com> "test with google"

    [reference-styale link][1]
    [1]:<https://google.com> "test with google"

<span style="font-family: Courier">
The title you want to give to the link is at the back of the web link, surrounded by parentheses or quotation marks.

### <span style="font-family: Courier">**Images**

<span style="font-family: Courier">
To be honest, I prefer the HTML notation for the Images, because it's just much more easier to control their sizes and characters.

<img src="./fatLogo.png" alt="the fat logo!" title="a fat logo for the blog" width=200 />

```
Markdown 
![The fat logo](./fatLogo.png "a fat logo of the blog")

HTML
<img src="./fatLogo.png" alt="the fat logo!" title="a fat logo for the blog" width=200 />
```

<span style="font-family: Courier">
Also, **mkdocs** seems to have different ideas about the location of the images and tries to modify it by adding a thing in the front, which is super weird.

### <span style="font-family: Courier">**Escaping Characters**

<span style="font-family: Courier">
To escape the characters, you just need to add a backslash (\) in front ofthe character you want to escape.

## <span style="font-family: Courier">Extended Syntax

<span style="font-family: Courier">
Extended syntax are created from the superset of the basic syntax, to add new features to the already powerful Markdown files.

### <span style="font-family: Courier">**Tables**

<span style="font-family: Courier">
Tables are added with three or more hyphens (---) to create each column's header, and use pipes (|) to separate each column. Pipes at either end of the table are added optionally.

<span style="font-family: Courier">
Also the size of the cell don't actually matter.

```HTML
Mardown
| Syntax     | Description |
|:-----------|------------:|
| Header     | Title       |
| Paragraph  | Text        |

HTML
<table>
    <thead>
        <tr class="header">
            <th>Syntax</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr class="odd">
            <td>Header</td>
            <td>Title</td>
        </tr>
        <tr class="even">
            <td>Paragraph</td>
            <td>Text</td>
        </tr>
    </tbody>
</table>
```
<span style="font-family: Courier">
You can set the alignment of the text inside the column by adding a colon (:) to the left, right, or on both sides of the hyphens (---). With HTML, you can add a CSS style to each table element.

    <td style="text-align: left;">Header</td>

| Syntax     | Description |
|:-----------|------------:|
| Header     | Title       |
| Paragraph  | Text        |

<span style="font-family: Courier">
You can do all sorts of formating inside the tables.

<span style="font-family: Courier">
If you want to escape the pipe (|) character in a table, you can use its HTML character code (`&#124;`).

### <span style="font-family: Courier">**Fenced Code Blocks**

<span style="font-family: Courier">
You can create a fenced code block by using three tick marks(```) or three tildes (~~~).

```HTML
Markdown
\```
{
    The code here
}
\```

HTML
<pre>
    <code>
        {
            &quot; The code here
        }
    </code>
</pre>
```

<span style="font-family: Courier">
You can add different colour highlighting according to the language by simply writing the language's name by the first three tick marks.

    ```HTML
    ```

### <span style="font-family: Courier">**Footnotes**

<span style="font-family: Courier">
To create a footnote reference, add a caret and an identifier inside brackets ([^1]). The Identifiers can be numbers or words, but they can't contain any space or tabs. The identifiers only correlate the footnote reference with the footnote itself. In the output, the footnotes are numbered sequentially.

<span style="font-family: Courier">
Add the footnote using another caret and identifier inside brackets with a colon and text (`[^1]: One footnote.`). You can put the footnotes anywhere except in lists, blocks, quotes and tables.

```HTML
Markdown
Here's a simple footnote,[^1] and another longer one.[^a_longer_footnote]

[^1]: The first smaller footnote.

[^a_longer_footnote]: This is a longer footnode and you can do lots of things.
    You can add paragraphs to your footnote by indenting them.
    `{can even add a code}`
    You can add as many paragraphs as you like


HTML
<p>
    Here's a simple footnote,<a href="#fn1" class="footnote-ref" id="fnref1"><sup>1</sup></a> and another longer one.<a href="#fn2" class="footnote-ref" id="fnref2"><sup>a_longer_footnote</sup></a>
</p>
<section class="footnotes">
    <hr />
    <ol>
        <li id="fn1"><p>The first smaller footnote.<a href="#fnref1" class="footnote-back"> </a></p></li>
        <li id="fn2">
            <p>The first smaller footnote.</p>
            <p>You can add paragraphs to your footnote by indenting them.</p>
            <p><code>{can even add a code}</code></p>
            <p>You can add as many paragraphs as you like
                <a href="#fnref2" class="footnote-back"> </a>
            </p>
        </li>
    </ol>
</section>
```

<p style="font-family: Courier">
    Here's a simple footnote,<a href="#fn1" class="footnote-ref" id="fnref1"><sup>1</sup></a> and another longer one.<a href="#fn2" class="footnote-ref" id="fnref2"><sup>a_longer_footnote</sup></a>
</p>

<span style="font-family: Courier">
The markdown notations doesn't seem to work, so I used the HTML ones.

### <span style="font-family: Courier">**Heading IDs**

<span style="font-family: Courier">
You can custom your heading's id by enclosing the custom ID in curly braces on the same line as the heading.

```
Markdown
### The Great Heading {#custom-id}

HTML
<h3 id="custom-id">The Great Heading</h3>
```

<span style="font-family: Courier">
You can create a link to your heading by creating a [standard link](#1) with the number sign (#) followed by the custom heading ID. But sadly, the markdown notation still doesn't work, I wonder...

```
Markdown
[Heading IDs](#heading-ids)

HTML
<a href="#heading-ids">Heading IDs</a>
```

### <span style="font-family: Courier">**Definition Lists**

```HTML
Markdown
First Term
: This is the definition of the first term.

Second Term
: This is the first definition of the second term.
: This is another definition of the second term.


HTML
<dl>
    <dt>First Term</dt>
    <dd>This is the definition of the first term.</dd>
    <dt>Second Term</dt>
    <dd>This is the first definition of the second term.</dd>
    <dd>This is another definition of the second term.</dd>
</dl>
```

<dl>
    <dt style="font-family: Courier">First Term</dt>
    <dd style="font-family: Courier">This is the definition of the first term.</dd>
    <dt style="font-family: Courier">Second Term</dt>
    <dd style="font-family: Courier">This is the first definition of the second term.</dd>
    <dd style="font-family: Courier">This is another definition of the second term.</dd>
</dl>

<span style="font-family: Courier">
No surprise that the markdown syntax still doesn't work. Consider this as a great opportunity to learn HTML (LOL).

### <span style="font-family: Courier">**Srikethrough**

<span style="font-family: Courier">
~~Strike through~~ the words by adding two tilde symbols (~~) on both sides of the words. But it seems that the strikethrough don't work with mkdocs.

### <span style="font-family: Courier">**Task Lists**

<span style="font-family: Courier">
Task lists can be created with a dash line (-) and brackets with a space ([ ]). If you finished the task, then add a x in the brackets ([x]).

```
Markdown
- [ ] Write some Markdown files
- [ ] Upload it to the website
```

 


















<section class="footnotes" style="font-family: Courier">
    <hr />
    <ol>
        <li id="fn1"><p>The first smaller footnote.<a href="#fnref1" class="footnote-back"> </a></p></li>
        <li id="fn2">
            <p>The first smaller footnote.</p>
            <p>You can add paragraphs to your footnote by indenting them.</p>
            <p><code>{can even add a code}</code></p>
            <p>You can add as many paragraphs as you like
                <a href="#fnref2" class="footnote-back"> </a>
            </p>
        </li>
    </ol>
</section>

