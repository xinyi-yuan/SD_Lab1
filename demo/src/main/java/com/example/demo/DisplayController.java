package com.example.demo;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;

import java.net.URL;
import java.util.ResourceBundle;

public class DisplayController implements Initializable {
    @FXML
    private NumberAxis tempAxis;
    @FXML
    private NumberAxis timeAxis;
    @FXML
    private LineChart<Number, Number> tempChart;
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        // Suppose to show the data
        XYChart.Series<Number, Number> series = new XYChart.Series<>();
        series.setName("Detected");
        // add data to the series
        series.getData().add(new XYChart.Data<>(-300, 10));
        series.getData().add(new XYChart.Data<>(-200, 20));
        series.getData().add(new XYChart.Data<>(-100, 30));
        series.getData().add(new XYChart.Data<>(0, 40));
        tempChart.getData().add(series);

    }
}