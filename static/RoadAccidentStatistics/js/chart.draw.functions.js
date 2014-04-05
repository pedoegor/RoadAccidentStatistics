
function getOptions(title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    trendlines = {};
    if (drawTrendLine) {
        for(var i = 0; i < trendLineNumber; i++) {
        if(isLinear)
            trendlines[i] = {};
        else
            trendlines[i] = {type: 'exponential'};
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
chartObjectMap["area"] = function(chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    return {
        object: new google.visualization.AreaChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber)
    };
};
chartObjectMap["line"] = function(chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    return {
        object: new google.visualization.LineChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber)
    };
};
chartObjectMap["column"] = function(chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    return {
        object: new google.visualization.ColumnChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber)
    };
};
chartObjectMap["bar"] = function(chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    return {
        object: new google.visualization.BarChart(document.getElementById(chartDiv)),
        options: getOptions(title, yAxisTitle, xAxisTitle, drawTrendLine, isLinear, trendLineNumber)
    };
};
chartObjectMap["bubble"] = function(chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber) {
    return {
        object: new google.visualization.BubbleChart(document.getElementById(chartDiv)),
        options: getOptions(title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, trendLineNumber)
    };
};
function draw2D(chartObject, chartDiv, chartTypeName, title, xAxisTitle, yAxisTitle, data, drawTrendLine, isLinear) {
    if (chartObject != null) {
        chartObject.clearChart();
    }
    chartContext = chartObjectMap[chartTypeName](chartDiv, title, xAxisTitle, yAxisTitle, drawTrendLine, isLinear, data[0].length - 1);
    chartObject = chartContext.object;
    chartObject.draw(google.visualization.arrayToDataTable(data), chartContext.options);
    return chartObject;
}
