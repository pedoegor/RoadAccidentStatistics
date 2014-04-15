function getOptions(title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    trendlines = {};
    if (trendType != null && trendType != "no") {
        for(var i = 0; i < trendLineNumber; i++) {
            trendlines[i] = {type: trendType};
        }
    }
    return {
        title: title,
        hAxis: {title: hAxisTitle, minValue: minH, maxValue: maxH},
        vAxis: {title: vAxisTitle, minValue: minV, maxValue: maxV},
        bubble: {
            textStyle: {
                fontSize: 10
            }
        },
        trendlines: trendlines
    };
}
chartObjectMap = {};
chartObjectMap["area"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    return {
        object: new google.visualization.AreaChart(document.getElementById(chartDiv)),
        options: getOptions(title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber)
    };
};
chartObjectMap["line"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    return {
        object: new google.visualization.LineChart(document.getElementById(chartDiv)),
        options: getOptions(title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber)
    };
};
chartObjectMap["column"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    return {
        object: new google.visualization.ColumnChart(document.getElementById(chartDiv)),
        options: getOptions(title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber)
    };
};
chartObjectMap["point"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    return {
        object: new google.visualization.ScatterChart(document.getElementById(chartDiv)),
        options: getOptions(title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber)
    };
};
chartObjectMap["bar"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber) {
    return {
        object: new google.visualization.BarChart(document.getElementById(chartDiv)),
        options: getOptions(title, vAxisTitle, hAxisTitle, minH, minV, maxH, maxV, trendType, trendLineNumber)
    };
};
chartObjectMap["bubble"] = function(chartDiv, title, hAxisTitle, vAxisTitle, minH, minV, maxH, maxV) {
    return {
        object: new google.visualization.BubbleChart(document.getElementById(chartDiv)),
        options: getOptions(title, vAxisTitle, hAxisTitle, minH, minV, maxH, maxV)
    };
};
chartObjectMap["sankey"] = function(chartDiv) {
    return {
        object: new google.visualization.Sankey(document.getElementById(chartDiv)),
        options: {
            sankey: {
                iterations: 50,
                node: {
                    label: {
                        fontName: 'Calibri',
                        fontSize: 12,
                        color: '#000',
                        bold: true,
                        italic: false
                    },
                    labelPadding: 6,
                    nodePadding: 80,
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

function findMin(data, index) {
    var min = 10000000;
    for(var i = 0; i < data.length; i++) {
        if(data[i][index] < min) min = data[i][index];
    }
    return min;
}

function findMax(data, index) {
    var max = -10000000;
    for(var i = 0; i < data.length; i++) {
        if(data[i][index] > max) max = data[i][index];
    }
    return max;
}

function drawTable(tableObject, tableDiv, data) {
    if (tableObject != null) {
        tableObject.clearChart();
    }
    tableObject = new google.visualization.Table(document.getElementById(tableDiv));
    tableObject.draw(data, {showRowNumber: true});
}

//chartObject, chartDiv, chartTypeName, data, title, hAxisTitle, vAxisTitle, hValueIndex, vValueIndex, trendType, trendNumber
function drawWithParameters(opts) {
    if (opts.chartObject != null) {
        opts.chartObject.clearChart();
    }
    if(opts.hValueIndex != null) {
        var minH = findMin(opts.data, opts.hValueIndex);
        var minV = findMin(opts.data, opts.vValueIndex);
        var maxH = findMax(opts.data, opts.hValueIndex);
        var maxV = findMax(opts.data, opts.vValueIndex);
    }
    var dataTable = google.visualization.arrayToDataTable(opts.data);
    chartContext = chartObjectMap[opts.chartTypeName](opts.chartDiv, opts.title, opts.hAxisTitle, opts.vAxisTitle,
        minH - minH / 10, minV - minV / 10, maxH + maxH / 10, maxV + maxV / 10, opts.trendType, opts.trendNumber);
    opts.chartObject = chartContext.object;
    opts.chartObject.draw(dataTable, chartContext.options);
    if(opts.chartTypeName == 'pie'){
        google.visualization.events.addListener(opts.chartObject, 'select', function(){alert(opts.chartObject.getSelection()[0].row)});
    }
    if(opts.drawTable == null || opts.drawTable == true)drawTable(info, 'info', dataTable);
}

