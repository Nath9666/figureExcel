<div class="border border-border rounded-lg bg-background p-6 shadow-sm"><div class="prose prose-sm md:prose-base lg:prose-lg max-w-none prose-headings:font-bold prose-a:text-blue-600" style="user-select: none;"><div id="top" class="">

<div align="center" class="text-center">
<h1>FIGUREEXCEL</h1>
<p><em>Transform Data into Insights Instantly and Visually</em></p>

<img alt="last-commit" src="https://img.shields.io/github/last-commit/Nath9666/figureExcel?style=flat&logo=git&logoColor=white&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/Nath9666/figureExcel?style=flat&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/Nath9666/figureExcel?style=flat&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Built with the tools and technologies:</em></p>
<img alt="Markdown" src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
</div>
<br>
<hr>
<h2>Table of Contents</h2>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#overview">Overview</a></li>
<li class="my-0"><a href="#getting-started">Getting Started</a>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><a href="#prerequisites">Prerequisites</a></li>
<li class="my-0"><a href="#installation">Installation</a></li>
<li class="my-0"><a href="#usage">Usage</a></li>
<li class="my-0"><a href="#testing">Testing</a></li>
</ul>
</li>
</ul>
<hr>
<h2>Overview</h2>
<p>figureExcel is a developer-focused tool that automates the generation and visualization of line charts from Excel data, making data analysis more efficient and visually consistent. It enables users to create dynamic, styled graphical representations of datasets with minimal manual effort.</p>
<p><strong>Why figureExcel?</strong></p>
<p>This project helps developers streamline data visualization workflows within Excel environments. The core features include:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0">🎯 <strong>[Feature]</strong>: Automated creation of line charts from Excel data, saving time and reducing manual effort.</li>
<li class="my-0">🖍️ <strong>[Feature]</strong>: Customizable visual styles through configuration files, ensuring consistent and appealing graphics.</li>
<li class="my-0">⚙️ <strong>[Feature]</strong>: Command-line parameters for flexible, dynamic chart generation tailored to specific needs.</li>
<li class="my-0">📊 <strong>[Feature]</strong>: Integrated data processing, sorting, and plotting capabilities for comprehensive analysis.</li>
<li class="my-0">🧩 <strong>[Feature]</strong>: Modular architecture with clear configuration and core modules, facilitating easy maintenance and extension.</li>
</ul>
<hr>
<h2>Getting Started</h2>
<h3>Prerequisites</h3>
<p>This project requires the following dependencies:</p>
<ul class="list-disc pl-4 my-0">
<li class="my-0"><strong>Programming Language:</strong> Python</li>
<li class="my-0"><strong>Package Manager:</strong> Conda</li>
</ul>
<h3>Installation</h3>
<p>Build figureExcel from the source and install dependencies:</p>
<ol>
<li class="my-0">
<p><strong>Clone the repository:</strong></p>
<pre><code class="language-sh">❯ git clone https://github.com/Nath9666/figureExcel
</code></pre>
</li>
<li class="my-0">
<p><strong>Navigate to the project directory:</strong></p>
<pre><code class="language-sh">❯ cd figureExcel
</code></pre>
</li>
<li class="my-0">
<p><strong>Install the dependencies:</strong></p>
<pre><code class="language-sh">❯ pip install -r requirements.txt
</code></pre>
</li>
</ol>
<h3>Usage</h3>
<p>Run the project with:</p>
<p><strong>Using python:</strong></p>
<pre><code class="language-sh">python -m app.main.py ./data/Classeur1.xlsx Date [[Données 1, 10, 15, Titre 1, #FF0000], [Données 2, 4, 15, Titre 2, #00FF00]]
</code></pre>
<h3>Testing</h3>
<p>Figureexcel uses the {<strong>test_framework</strong>} test framework. Run the test suite with:</p>
<pre><code class="language-sh">python -m pytest
</code></pre>
<hr>
<div align="left" class=""><a href="#top">⬆ Return</a></div>
<hr></div></div></div>





---


## Table of Contents


* [Overview](#overview)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Testing](#testing)


---


## Overview


figureExcel is a developer-focused tool that automates the generation and visualization of line charts from Excel data, making data analysis more efficient and visually consistent. It enables users to create dynamic, styled graphical representations of datasets with minimal manual effort.


**Why figureExcel?**


This project helps developers streamline data visualization workflows within Excel environments. The core features include:


* 🎯 **[Feature]**: Automated creation of line charts from Excel data, saving time and reducing manual effort.
* 🖍️ **[Feature]**: Customizable visual styles through configuration files, ensuring consistent and appealing graphics.
* ⚙️ **[Feature]**: Command-line parameters for flexible, dynamic chart generation tailored to specific needs.
* 📊 **[Feature]**: Integrated data processing, sorting, and plotting capabilities for comprehensive analysis.
* 🧩 **[Feature]**: Modular architecture with clear configuration and core modules, facilitating easy maintenance and extension.


---


## Getting Started


### Prerequisites


This project requires the following dependencies:


* **Programming Language:** Python
* **Package Manager:** Conda


### Installation


Build figureExcel from the source and install dependencies:


1. **Clone the repository:**
   ```sh
   ❯ git clone https://github.com/Nath9666/figureExcel
   ```
1. **Navigate to the project directory:**
   ```sh
   ❯ cd figureExcel
   ```
1. **Install the dependencies:**
   ```sh
   ❯ pip install -r requirements.txt
   ```


### Usage


Run the project with:


**Using python:**


```sh
python main.py ./data/Classeur1.xlsx Date [[Données 1, 10, 15, Titre 1, #FF0000], [Données 2, 4, 15, Titre 2, #00FF00]]
```


### Testing


Figureexcel uses the {**test_framework**} test framework. Run the test suite with:


```sh
python -m pytest
```


---



---

---

## Table of Contents

* [Overview](#overview)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Testing](#testing)

---

## Overview

figureExcel is a developer-focused tool that automates the generation and visualization of line charts from Excel data, making data analysis more efficient and visually consistent. It enables users to create dynamic, styled graphical representations of datasets with minimal manual effort.

**Why figureExcel?**

This project helps developers streamline data visualization workflows within Excel environments. The core features include:

* 🎯 **[Feature]**: Automated creation of line charts from Excel data, saving time and reducing manual effort.
* 🖍️ **[Feature]**: Customizable visual styles through configuration files, ensuring consistent and appealing graphics.
* ⚙️ **[Feature]**: Command-line parameters for flexible, dynamic chart generation tailored to specific needs.
* 📊 **[Feature]**: Integrated data processing, sorting, and plotting capabilities for comprehensive analysis.
* 🧩 **[Feature]**: Modular architecture with clear configuration and core modules, facilitating easy maintenance and extension.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

* **Programming Language:** Python
* **Package Manager:** Conda

### Installation

Build figureExcel from the source and install dependencies:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Nath9666/figureExcel
   ```
2. **Navigate to the project directory:**
   ```sh
   cd figureExcel
   ```
3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Usage

Run the project with:

**Using python:**

```sh
python main.py ./data/Classeur1.xlsx Date [[Données 1, 10, 15, Titre 1, #FF0000], [Données 2, 4, 15, Titre 2, #00FF00]]
```

### Testing

Figureexcel uses the {**test_framework**} test framework. Run the test suite with:

```sh
python -m pytest
```

---

---
