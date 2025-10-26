<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance Absence Record</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background: white;
        }
        
        h1 {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: black;
        }
        
        table {
            width: 100%;
            max-width: 1000px;
            margin: 0 auto;
            border-collapse: collapse;
            border: 2px solid black;
        }
        
        th, td {
            border: 1px solid black;
            padding: 0;
            text-align: center;
            font-size: 12px;
            font-weight: normal;
            height: 40px;
            vertical-align: middle;
            position: relative;
        }
        
        th {
            background-color: white;
            font-weight: bold;
            padding: 8px;
        }
        
        .sl-no {
            font-weight: bold;
            width: 60px;
            padding: 8px;
        }
        
        .month-col {
            width: 80px;
        }
        
        .divided-cell {
            display: flex;
            height: 100%;
        }
        
        .cell-left, .cell-right {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            border-right: 1px solid #666;
        }
        
        .cell-right {
            border-right: none;
        }
        
        .total-row {
            font-weight: bold;
        }
        
        .total-row td {
            padding: 8px;
        }
        
        .legend {
            margin: 20px auto;
            max-width: 1000px;
            font-size: 12px;
            text-align: center;
            color: #666;
        }
        
        @media print {
            body {
                margin: 10px;
            }
            .legend {
                margin: 10px auto;
            }
        }
    </style>
</head>
<body>
    <h1>Attendance Absence Record</h1>
    
    <div class="legend">
        Each cell is divided: Left section | Right section (for tracking dual attendance data)
    </div>
    
    <table>
        <thead>
            <tr>
                <th class="sl-no">SLNO</th>
                <th class="month-col">APR</th>
                <th class="month-col">MAY</th>
                <th class="month-col">JUN</th>
                <th class="month-col">JULY</th>
                <th class="month-col">AUG</th>
                <th class="month-col">SEP</th>
                <th class="month-col">OCT</th>
                <th class="month-col">NOV</th>
                <th class="month-col">DEC</th>
                <th class="month-col">JAN</th>
                <th class="month-col">FEB</th>
                <th class="month-col">MAR</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="sl-no">1</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
 <tr>
                <td class="sl-no">2</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">3</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">4</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">5</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">6</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">7</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">8</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">9</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">10</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">11</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">12</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">13</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">14</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">15</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">16</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
 <tr>
                <td class="sl-no">17</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
                <td class="sl-no">18</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">19</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">20</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">21</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">22</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">23</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">24</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">25</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">26</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">27</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">28</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">29</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>
            <tr>
                <td class="sl-no">30</td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
                <td><div class="divided-cell"><div class="cell-left"></div><div class="cell-right"></div></div></td>
            </tr>

            <tr class="total-row">
                <td class="sl-no">TOTAL</td>
                <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
            </tr>
            <tr class="total-row">
                <td class="sl-no">ABSENT</td>
                <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
            </tr>
            <tr class="total-row">
                <td class="sl-no">G.TOTAL</td>
                <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
            </tr>
            <tr class="total-row">
                <td class="sl-no">SIGN</td>
                <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
            </tr>
        </tbody>
    </table>
</body>
</html>>