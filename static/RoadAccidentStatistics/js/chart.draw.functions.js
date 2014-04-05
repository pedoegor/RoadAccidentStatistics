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
function drawWithParameters(chartObject, chartDiv, chartTypeName, title, xAxisTitle, yAxisTitle, data, trendType) {
    if (chartObject != null) {
        chartObject.clearChart();
    }
    chartContext = chartObjectMap[chartTypeName](chartDiv, title, xAxisTitle, yAxisTitle, trendType, data[0].length - 1);
    chartObject = chartContext.object;
    chartObject.draw(google.visualization.arrayToDataTable(data), chartContext.options);
    return chartObject;
}
