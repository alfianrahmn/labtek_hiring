## Test

### Technical Test & Case Study: Important Information

This technical test and case study are designed to evaluate your technical skills and analytical abilities. Please note that the brand name used in this case study is purely illustrative and does not represent any real client conditions.

You are required to complete two separate tasks, each to be placed in its own folder. All completed tasks should be submitted within a single GitHub repository, which must be set to public. The expected repository structure is as follows:

```
questions
├── technical
│   ├── tech_1
│   │   ├── main.py
│   │   └── data.csv (optional, for test case data)
│   └── tech_2
│       ├── main.py / query.sql
│       └── data.csv (optional, for test case data)
└── case
    └── case_1
        └── README.md (Contains assumptions, learnings, and challenges encountered during the case study)
```

The submission process involves sending the GitHub repository link to `saska@labtekindie.com`. You will have a specific deadline for submission, as mentioned in the email. The estimated time required to complete both tasks is approximately 2-3 hours.

### Technical Test

This section contains two technical challenges. You are expected to answer using Python. You only need to submit a file containing the function with the specified input and return output. It's acceptable to use built-in functions, or you can write solutions from scratch. If you use external tools like ChatGPT or Google, explain their purpose in your source code comments. You're expected to spend 60-90 minutes on all technical questions, and within that timeframe, feel free to add unit tests, test cases, or anything else you deem necessary.

#### Tech 1 - Initiator of Discount

You are working within an e-commerce company and want to track merchant discounting behavior. One of the products offered is the ability for brands to track the price of their products sold by their retailers. To provide better insights and information on their prices, there is also an attempt to track the initiator of discount. The first part of identifying an initiator of discount is to figure out when is the earliest that a product reduces their price in a timeframe.

**Question:**

You will be given a string of 'N' integer values (between 1 and 100), separated by spaces. Each integer represents the price of a product (between 1 and 50,000). Your task is to identify the 0-based position 'i' where a price reduction occurred. A price reduction is defined as the current price being smaller than both the previous price and the price at the beginning of the period.

* If no price reduction occurs, return `0`.
* If a price reduction occurs, return the first position 'i' where it happens.

**Examples:**

* Input: "3 3 3 3"
* Output: 0

* Input: "3 4 3"
* Output: 0

* Input: "3 4 1"
* Output: 2

**Challenge/Bonus:**

Consider a scenario where the price data might have occasional, short-lived "noise" (e.g., a single price point spikes up or down briefly before returning to the general trend). How would you modify your approach to identify significant, sustained price reductions while being robust to such noise? Describe your approach and, if possible, provide a pseudocode example.

#### Tech 2 - Biggest Contributor

For this test, you'll be given a CSV file containing a subset of freelance activity data. You can use Python (e.g., pandas, polars) or SQL to solve this problem.

**Questions:**

Given the CSV, which contains freelance activity data from several contributors (identified by the 'email' field inside the `_meta` column), identify the contributor who has provided the most freelance activity based on:

* The number of projects contributed across all dates.
* The total salary in Rupiah contributed across all dates.

Your output should be an `out.csv` file with the following format:

```
qualification,top_contributor
project_count,email1@example.com
total_salary_idr,email1@example.com
```

The `total_earnings_idr` column is the total earnings in Rupiah from the start of the freelancer's history. Your task is to find out which project role (e.g., "Data Analyst," "Web Developer") had the most earnings during **Q1 2024 (January 1st, 2024 to March 31st, 2024)**. Output the top 10 earning project roles using the following format, sorted from the highest earnings to lower:

```
client_company_id,project_role,earnings,hourly_rate_idr
```

**Challenge/Bonus:**

Imagine the CSV data is extremely large and cannot fit into memory. How would you approach solving the "Biggest Contributor" problem (both parts) using a method that handles large datasets efficiently? Discuss potential tools or techniques (e.g., Dask, PySpark, database streaming) and briefly explain your chosen strategy.

---

### Case Study

This case study is designed to be answered within 60-90 minutes. You are free to answer in English or Indonesian.

#### Case Study - Designing an AI-Powered Application with Heterogeneous User Data

One of the challenges in building AI-powered applications is integrating diverse data sources and managing loosely connected user entities. This often involves combining structured and unstructured data where user identification can be inconsistent (e.g., some users are identified by email, some by phone numbers, and in worst-case scenarios, only by their full name).

**Scenario:**

You are tasked with designing an AI-powered application that needs to leverage both structured and unstructured data to provide personalized experiences. User data is scattered across various systems, with no single, unified identifier. For instance:

* **Structured Data:** Transactional records (e.g., purchase history) with user emails.
* **Unstructured Data:** Customer service chat logs (with user phone numbers or full names), social media posts (with usernames that might or might not map to real names), and product reviews.
* **User Identifiers:** Some systems use email, others phone numbers, and some only full names. There's no guaranteed unique identifier across all sources for a single user.

**Questions:**

1.  As an AI Engineer, outline your process for designing and building such an application. Focus on how you would approach the data integration and entity resolution challenges to create a unified user profile for the AI model.
2.  What techniques and tools would you consider for extracting relevant information from the unstructured data and linking it to existing structured data?
3.  How would you handle the ambiguity and potential errors arising from loosely connected user entities (e.g., multiple users with the same name)? Discuss strategies for improving user entity resolution and maintaining data quality.
4.  Describe your approach to designing the AI model(s) given the heterogeneous data and the need for personalized experiences.

You are expected to provide your answers in a `README.md` file, approximately 500 words in length, and include code (pseudocode, SQL, or Python) if necessary.
