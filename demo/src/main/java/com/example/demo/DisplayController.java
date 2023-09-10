package com.example.demo;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Button;

import java.io.File;
import java.io.FileNotFoundException;
import java.net.URL;
import java.util.ArrayList;
import java.util.ResourceBundle;
import java.util.Scanner;

public class DisplayController implements Initializable {
    private ArrayList<Integer> timeArr = new ArrayList<>();
    private ArrayList<Double> tempArr = new ArrayList<>();
    @FXML
    private Button visualButton;
    @FXML
    private NumberAxis tempAxis;
    @FXML
    private NumberAxis timeAxis;
    @FXML
    private LineChart<Number, Number> tempChart;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        //int[] time = {-300, -250, -200, -170, -150, -100, -50, 0};
        //double[] temp = {23, 24, 23, 25, 23.5, 21, 25, 20};
        try {
            readCSV();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        visualizeGraph(timeArr, tempArr);
    }

    // fahrenheit = (celsius * 9/5) + 32

    private void readCSV() throws FileNotFoundException {
        Scanner scan = new Scanner(new File("C:\\Learning\\Senior Design\\SD_Lab1\\demo\\src\\main\\resources\\com\\example\\demo\\testTempData.csv"));
        String[] record;
        while(scan.hasNext()) {
            record = scan.nextLine().split(",");
            timeArr.add(Integer.parseInt(record[0]));
            tempArr.add(Double.parseDouble(record[1]));
        }
    }

    /*
    This function add data to the graph
     */
    private void visualizeGraph(ArrayList<Integer> time, ArrayList<Double> temp) {
        // Suppose to show the data
        XYChart.Series<Number, Number> series = new XYChart.Series<>();
        series.setName("Detected");
        // add data to the series
        if (time.size() == temp.size()) {
            for (int i = 0; i < time.size(); i ++) {
                series.getData().add(new XYChart.Data<>(time.get(i), temp.get(i)));
            }
        }
        tempChart.getData().add(series);
        /*
        series.getData().add(new XYChart.Data<>(-300, 10));
        series.getData().add(new XYChart.Data<>(-200, 20));
        series.getData().add(new XYChart.Data<>(-100, 30));
        series.getData().add(new XYChart.Data<>(0, 40));
        tempChart.getData().add(series);
         */
    }
}