package gui;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class ViewController {

	@FXML
	private Button btMyButton;
        @FXML
        private TextField Text1;
	
	@FXML
	public void onMyButtonClick() {
		System.out.println("Hello!");
	}

    
    
}
