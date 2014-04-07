function getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    trendlines = {};
    if (trendType != "no") {
        for(var i = 0; i < trendLineNumber; i++) {
            trendlines[i] = {type: trendType};
        }
    }
    return {
        title: title,
        hAxis: {title: xAxisTitle},
        vAxis: {title: yAxisTitle},
        trendlines: trendlines
    };
}
chartObjectMap = {};
chartObjectMap["area"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.AreaChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["line"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.LineChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["column"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.ColumnChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["point"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.ScatterChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["bar"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.BarChart(document.getElementById(chartDiv)),
        options: getOptions(title, yAxisTitle, xAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["bubble"] = function(chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendLineNumber) {
    return {
        object: new google.visualization.BubbleChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, trendType, trendLineNumber)
    };
};
chartObjectMap["sankey"] = function(chartDiv) {
    return {
        object: new google.visualization.Sankey(document.getElementById(chartDiv)),
        options: {
            sankey: {
                node: {
                    label: {
                        fontName: 'Times-Roman',
                        fontSize: 12,
                        color: '#000',
                        bold: true,
                        italic: false
                    },
                    labelPadding: 6,
                    nodePadding: 10,
                    width: 5
                }
            }
        }
    };
};
chartObjectMap["pie"] = function(chartDiv, title) {
    return {
        object: new google.visualization.PieChart(document.getElementById(chartDiv)),
        options: {
            title: title,
            is3D: true
        }
    };
};
function drawWithParameters(chartObject, chartDiv, chartTypeName, data, title, xAxisTitle, yAxisTitle, trendType, trendNumber) {
    if (chartObject != null) {
        chartObject.clearChart();
    }
    chartContext = chartObjectMap[chartTypeName](chartDiv, title, xAxisTitle, yAxisTitle, trendType, trendNumber);
    chartObject = chartContext.object;
    chartObject.draw(data, chartContext.options);
    return chartObject;
}
function drawTable(tableObject, tableDiv, data) {
    if (tableObject != null) {
        tableObject.clearChart();
    }
    tableObject = new google.visualization.Table(document.getElementById(tableDiv));
    tableObject.draw(data, {showRowNumber: true});
    return tableObject;
}
