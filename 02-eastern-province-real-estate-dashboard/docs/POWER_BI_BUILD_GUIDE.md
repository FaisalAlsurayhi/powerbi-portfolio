# Power BI Build Guide

Project name:

**Eastern Province Real Estate Market Dashboard**

Dataset:

`data/eastern_province_real_estate_transactions.csv`

Goal:

Build a 4-page Power BI report that analyzes real estate transactions across Khobar, Dammam, Dhahran, and Jubail.

## Step 1: Load The Data

1. Open Power BI Desktop.
2. Select **Get data**.
3. Choose **Text/CSV**.
4. Open:
   `eastern_province_real_estate_transactions.csv`
5. Click **Transform Data**.
6. In Power Query, rename the table to:
   `RealEstate`

## Step 2: Check Column Types

Make sure the columns are set like this:

| Column | Type |
| --- | --- |
| `Transaction_ID` | Text |
| `Date` | Date |
| `City` | Text |
| `District` | Text |
| `Property_Type` | Text |
| `Segment` | Text |
| `Area_sqm` | Whole Number |
| `Sale_Price_SAR` | Whole Number |
| `Price_per_sqm` | Whole Number |
| `Transaction_Type` | Text |

Then click **Close & Apply**.

## Step 3: Create Measures

1. Go to the **Data** or **Report** view.
2. Right-click the `RealEstate` table.
3. Click **New measure**.
4. Copy the measures from `DAX_MEASURES.md`.

Start with these first:

- `Total Transactions`
- `Total Sales Value`
- `Average Sale Price`
- `Average Price per sqm`
- `Total Area Sold`
- `Residential Share`
- `Commercial Share`

## Step 4: Page 1 - Market Overview

Page name:

**Market Overview**

Purpose:

Show the overall market size and monthly direction.

Visuals:

1. KPI Card: `Total Transactions`
2. KPI Card: `Total Sales Value`
3. KPI Card: `Average Sale Price`
4. KPI Card: `Average Price per sqm`
5. Line chart:
   - X-axis: `Date`
   - Y-axis: `Total Sales Value`
   - Title: `Monthly Sales Value`
6. Column chart:
   - X-axis: `City`
   - Y-axis: `Total Transactions`
   - Title: `Transactions by City`
7. Donut chart:
   - Legend: `Segment`
   - Values: `Total Sales Value`
   - Title: `Sales Value by Segment`

Slicers:

- `City`
- `Property_Type`
- `Segment`

Suggested insight text:

`The dashboard compares transaction volume, sales value, and price per square meter across major Eastern Province cities. Khobar and Dammam usually lead by activity, while Dhahran tends to show higher average prices.`

## Step 5: Page 2 - City Comparison

Page name:

**City Comparison**

Purpose:

Compare Khobar, Dammam, Dhahran, and Jubail.

Visuals:

1. Clustered bar chart:
   - Y-axis: `City`
   - X-axis: `Total Sales Value`
   - Title: `Sales Value by City`
2. Clustered bar chart:
   - Y-axis: `City`
   - X-axis: `Average Price per sqm`
   - Title: `Average Price per sqm by City`
3. Matrix:
   - Rows: `City`
   - Columns: `Property_Type`
   - Values: `Total Transactions`
   - Title: `Transaction Mix by City and Property Type`
4. Scatter chart:
   - X-axis: `Average Price per sqm`
   - Y-axis: `Total Transactions`
   - Size: `Total Sales Value`
   - Details: `City`
   - Title: `Market Position by City`

Slicers:

- `Segment`
- `Transaction_Type`

Suggested insight text:

`City comparison helps separate high-volume markets from high-price markets. A city can have fewer transactions but still show strong value if price per square meter is high.`

## Step 6: Page 3 - Property Type Analysis

Page name:

**Property Type Analysis**

Purpose:

Show which property types drive transactions and value.

Visuals:

1. Bar chart:
   - Y-axis: `Property_Type`
   - X-axis: `Total Sales Value`
   - Title: `Sales Value by Property Type`
2. Bar chart:
   - Y-axis: `Property_Type`
   - X-axis: `Average Price per sqm`
   - Title: `Average Price per sqm by Property Type`
3. Column chart:
   - X-axis: `Property_Type`
   - Y-axis: `Total Transactions`
   - Title: `Transactions by Property Type`
4. Donut chart:
   - Legend: `Segment`
   - Values: `Total Transactions`
   - Title: `Residential vs Commercial Transaction Share`

Slicers:

- `City`
- `Date`

Suggested insight text:

`Apartments and villas usually drive residential activity, while commercial units have higher price per square meter. Land can create large transaction value because of larger area sizes.`

## Step 7: Page 4 - District Insights

Page name:

**District Insights**

Purpose:

Find active and high-value districts.

Visuals:

1. Table:
   - `District`
   - `City`
   - `Total Transactions`
   - `Total Sales Value`
   - `Average Price per sqm`
2. Bar chart:
   - Y-axis: `District`
   - X-axis: `Average Price per sqm`
   - Title: `Top Districts by Price per sqm`
3. Bar chart:
   - Y-axis: `District`
   - X-axis: `Total Sales Value`
   - Title: `Top Districts by Sales Value`
4. Card:
   - `Total Area Sold`

Slicers:

- `City`
- `Property_Type`
- `Segment`

Suggested insight text:

`District-level analysis helps identify whether market value is concentrated in a few premium areas or spread across the city.`

## Design Style

Use a clean business style:

- Background: very light gray or white
- Main accent: deep green
- Secondary accent: dark blue
- Cards: white background, subtle border
- Keep charts simple and avoid too many colors

Suggested colors:

- Dark green: `#0B5D4D`
- Blue: `#1F4E79`
- Gold accent: `#C8A24A`
- Light background: `#F7F8FA`
- Dark text: `#1F2933`

## Final Checklist

- All pages have clear titles.
- KPI cards are aligned.
- Slicers are consistent.
- Currency fields show SAR.
- Percent fields show percentage.
- Page 1 gives the overview.
- Pages 2-4 give deeper analysis.
- Save the file as:
  `Eastern_Province_Real_Estate_Dashboard.pbix`
