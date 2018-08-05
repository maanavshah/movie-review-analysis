import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Samr extends JFrame {
	JPanel panel = new JPanel();

	Samr() throws IOException {
		super("Sentiment Analysis on Movie Reviews");
		setSize(700, 350);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		add(panel);
		setVisible(true);
		JButton button = new JButton("Analyze Movies");
		JPanel buttonPanel = new JPanel();
		buttonPanel.add(button);
		panel.add(buttonPanel);
		button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setVisible(false);
				System.exit(0);
			}
		});
		setLocationRelativeTo(null);
	}

	public static void main(String[] args) throws IOException {
		new Samr().setVisible(true);
	}
}