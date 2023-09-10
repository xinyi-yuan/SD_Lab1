package com.example.demo;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.control.Label;

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
        timeAxis.setLowerBound(300);
        timeAxis.setUpperBound(0);
        timeAxis.setTickUnit(100);
    }
}