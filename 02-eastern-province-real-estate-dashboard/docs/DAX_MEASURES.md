# DAX Measures

Use table name:

`RealEstate`

If Power BI imports the table with a different name, either rename it to `RealEstate` or update the table name in the formulas.

## Core Measures

```DAX
Total Transactions =
COUNTROWS(RealEstate)
```

```DAX
Total Sales Value =
SUM(RealEstate[Sale_Price_SAR])
```

```DAX
Average Sale Price =
AVERAGE(RealEstate[Sale_Price_SAR])
```

```DAX
Average Price per sqm =
AVERAGE(RealEstate[Price_per_sqm])
```

```DAX
Total Area Sold =
SUM(RealEstate[Area_sqm])
```

```DAX
Residential Sales Value =
CALCULATE(
    [Total Sales Value],
    RealEstate[Segment] = "Residential"
)
```

```DAX
Commercial Sales Value =
CALCULATE(
    [Total Sales Value],
    RealEstate[Segment] = "Commercial"
)
```

```DAX
Residential Share =
DIVIDE([Residential Sales Value], [Total Sales Value])
```

```DAX
Commercial Share =
DIVIDE([Commercial Sales Value], [Total Sales Value])
```

## Time Measures

Create these after you make sure `Date` is set as a Date column.

```DAX
Monthly Sales Value =
[Total Sales Value]
```

```DAX
Previous Month Sales =
CALCULATE(
    [Total Sales Value],
    DATEADD(RealEstate[Date], -1, MONTH)
)
```

```DAX
Monthly Sales Change =
[Total Sales Value] - [Previous Month Sales]
```

```DAX
Monthly Sales Change % =
DIVIDE([Monthly Sales Change], [Previous Month Sales])
```

## Ranking Measures

```DAX
City Rank by Sales =
RANKX(
    ALL(RealEstate[City]),
    [Total Sales Value],
    ,
    DESC
)
```

```DAX
District Rank by Price per sqm =
RANKX(
    ALL(RealEstate[District]),
    [Average Price per sqm],
    ,
    DESC
)
```

## Formatting Suggestions

- `Total Sales Value`: Currency, SAR, no decimals
- `Average Sale Price`: Currency, SAR, no decimals
- `Average Price per sqm`: Currency, SAR, no decimals
- `Residential Share`: Percentage, 1 decimal
- `Commercial Share`: Percentage, 1 decimal
- `Monthly Sales Change %`: Percentage, 1 decimal
