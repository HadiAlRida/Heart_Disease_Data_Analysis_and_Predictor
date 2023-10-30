<img  src="readme\title1.svg"/>

<div>

> Hello world! This is the project’s summary that describes the project, plain and simple, limited to the space available.
> **[PROJECT PHILOSOPHY](#project-philosophy) • [PROTOTYPING](#prototyping) • [TECH STACKS](#stacks) • [IMPLEMENTATION](#demo) • [HOW TO RUN?](#run)**

</div>

<br><br>

<!-- project philosophy -->

<a  name="philosophy" ></a>
<img  src="readme/title2.svg" id="project-philosophy"/>

> A Python-based ETL (Extract, Transform, Load) project aimed at processing data from various web sources, and subsequently storing it in a tabular database (PostgreSQL), with the objective of facilitating comprehensive analysis Disease disease data

> Heart Disease Analysis and Predictor Project, also aims to predict the probabilities if this might occur in the near future based on the data analyzed.<br>

### User Types

1. Healthcare Practitioners
2. Policy Makers.
3. Data Analysts and Scientists.
4. Policy Makers.
5. Journalist.

<br>

### User Stories

1.  Healthcare Practitioners:

    I want to access project insights to improve patient care, identify at-risk populations, and enhance clinical decision-making.
    I want to use findings for early intervention and personalized treatment strategies.
    I want to benefit from understanding disease trends to allocate resources effectivelys.

2.  Policy Makers:

    I want to utilize project data to inform evidence-based public health policies and initiatives.
    I want to address disease prevalence, risk factors, and preventive measures.
    I want to make informed decisions to enhance community health outcomes.

3.  Data Analysts and Scientists:

    I want to analyze data for research, modeling, and in-depth understanding of cardiovascular disease trends.
    I want to develop predictive models to identify risk factors and potential interventions.
    I want to contribute to scientific advancements in the field.

4.  Public Health Officials:

    I want to leverage project insights for public health campaigns and interventions.
    I want to prioritize resource allocation for prevention and awareness programs.
    I want to monitor and respond to changing disease patterns effectively.

5.  General Public:

    I want to gain knowledge about cardiovascular disease risks and prevention.
    I want to make informed lifestyle choices to reduce the risk of heart-related conditions.
    I want to understand the impact of heart health on personal well-being.

<br><br>

<!-- Prototyping -->

### Logger File

| LogIn |
| ----- |

<img  src="readme\logger.png"  id="prototyping"/>

### Data Tables Schema

<img  src="readme\Copy of db_Heart.png"  id="prototyping"/>

### Power BI Report Screenshots

#### landing Page

<img src= "readme\Landing_Page.png" id="prototyping"/>

#### Overview Page

<img src= "readme\Overview.png" id="prototyping"/>

#### Epidemiology Page

<img src= "readme\epidemiology.png" id="prototyping"/>

#### Etiology Page

<img src= "readme\etiology.png" id="prototyping"/>

#### Classification and Prediction Page

<img src= "readme\classification and evaluating.png" id="prototyping"/>

<br><br>
<br><br>

<!-- Implementation -->

<a  name="Demo"></a>
<img  src="readme/title4.svg" id="#demo" />

<br>

Heart Disease Analytics is built using the following technologies:

## Frontend

Interactive PowerBI Dashboard:
A central dashboard where viewers can view:

1. Epidemiological Indicators: Graphs, charts and visualizations displaying key Health metrics over time.
2. Cohort Studies Analysis:Cohort Studies Analysis: Conduct comprehensive analysis of cohort studies to investigate trends, risk factors, and outcomes in a defined group over time, providing valuable insights into the factors influencing specific health or research outcomes.
3. Predictive Analysis: A visualization of the ML model's performance about occurence of disease compared to actual data.
4. Interactive filters: options to filter data by date, region,type of disease,sex, or specific economic indicatiors for customized views.

<br>

## Backend

1. Automation.
2. ETL Pipeline: using python and pandas, raw data is extracted, transformed into a usable format and loaded into postgreSQL database.
3. Database: Schema Design - Data Integrity - Backup & Recovery.
4. Machine Learning & Predictive Analysis: Model Training - Evaluation and Prediction.

<br>

<br>

<!-- Tech stacks -->

<a  name="Stack"  ></a>
<img  src="readme\title5.svg" id="Stack"/>

<br><br>

1. SQL: SQL was used for efficient data retrieval and manipulation, facilitating the organization and preprocessing of medical data for analysis.
2. Python: Python's versatility was crucial for data extraction, transformation, and loading (ETL) tasks, allowing the creation of predictive models and statistical analysis, contributing to a comprehensive understanding of heart disease factors.
3. DAX (Data Analysis Expressions): DAX and Power Query seamlessly integrated with Power BI, enabling the creation of dynamic, interactive reports and dashboards. DAX provided powerful calculations and expressions.
4. Power Query: Power Query was essential for data transformation and cleansing, ensuring clean and accurate data for analysis and report generation.

### Machine Learning (ML) component

Using sickit-learn, we analyze the health data, training predictive models and deploying them for real-time predictions.

Data Collection & Preprocessing.
Model Selection & Training
Model Evaluation.
Model Deployment

ML model

#### Data Processing

<img src= "readme\Data Processing.png" id="Stack"/>

#### Training

<img src= "readme\training.png" id="Stack"/>

#### Predicting and Evaluating

<img src= "readme\predicting and evaluating.png" id="Stack"/>

#### evaluating

<img src= "readme\evaluating.png" id="Stack"/>

#### Data Processing

<img src= "readme\Data Processing.png" id="Stack"/>

#### Training

<img src= "readme\training.png" id="Stack"/>

#### Predicting and Evaluating

<img src= "readme\predicting and evaluating.png" id="Stack"/>

#### evaluating4

<img src= "readme\evaluating.png" id="Stack"/>

### model deployment

<img src= "readme\deployment.png" id="Stack"/>

### Prerequisites

**Hardware & Software**:

- A computer/server with sufficient RAM (minimum 8gb ram) and processing power.
- Operating system: Linux (preferred for production) or Windows.
- Required software: Python (3.x), PostgreSQL, Git (for version control), and any other specific software packages.

**Dependencies**:

- Install the necessary Python libraries: `Pandas`, `scikit-learn`, `numpy`, `xgboost`.
- Install database connectors/drivers for PostgreSQL.

### **Setting Up the Environment**:

**Clone the Repository**:

```sh

git clone https://github.com/HADIRIDA4/Heart_Disease_Data_Analysis_and_Predictor

```

**Set Up the Database**:

- Start the PostgreSQL server.
- Create a new database and user with the appropriate permissions.
- Run any initialization scripts to set up tables or initial.

### **Running the Backend**:

**Start the Data Ingestion & ETL Process**:
`python data_ingestion_script.py`

You should be able to check the app.log file to see the ETL work.

As for the dashboard access: Please use this link "public powerbi link" to access your data.
