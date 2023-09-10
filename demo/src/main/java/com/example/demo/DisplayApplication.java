package com.example.demo;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;

import java.io.IOException;

public class DisplayApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(DisplayApplication.class.getResource("temp-view.fxml"));

        /* This block is used to test out if the data works, but need to change the root of Scene to tempChart
        final NumberAxis timeAxis = new NumberAxis();
        final NumberAxis tempAxis = new NumberAxis();
        final LineChart<Number,Number> tempChart =
                new LineChart<>(timeAxis,tempAxis);
        XYChart.Series<Number, Number> series = new XYChart.Series<>();
        series.setName("Hi");

        series.getData().add(new XYChart.Data<>(-300, 10));
        series.getData().add(new XYChart.Data<>(-200, 20));
        series.getData().add(new XYChart.Data<>(-100, 30));
        series.getData().add(new XYChart.Data<>(0, 40));
        tempChart.getData().add(series);
         */

        // Change fxmlLoad.load() to tempChart to see data
        Scene scene = new Scene(fxmlLoader.load(), 500, 300);
        stage.setTitle("Temperature Display");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}