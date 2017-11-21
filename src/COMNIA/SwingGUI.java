package COMNIA;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;

public class SwingGUI
{
	final int WIDTH = 800;
	final int HEIGHT = 600;
	
	private	JFrame frame;
	private JPanel panelSidebar;
	
	public SwingGUI()
	{
		initGUI();
	}
	
	private void initGUI()
	{
		// Main JFrame
		frame = new JFrame("COMNIA");
		frame.setSize(800, 600);
		frame.setLayout(new GridLayout(1,2));
		frame.setVisible(true);
		
		// Left Sidebar
		panelSidebar = new JPanel();
		panelSidebar.setLayout(new CardLayout());
		frame.add(panelSidebar);
		
		// Test Button
		JButton testButton = new JButton();
		testButton.setBounds(frame.getWidth()/2 - 50,frame.getHeight()/2 - 20, 100,40);
		frame.add(testButton);
		
		for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
			System.out.println(info);
		}
		
		createMenuBar();
	}
	
	private void createMenuBar()
	{
		JMenuBar menubar = new JMenuBar();
		
		JMenu file = new JMenu("File");
		file.setMnemonic(KeyEvent.VK_F);

		JMenuItem preferencesMenuItem = new JMenuItem("Preferences");
		preferencesMenuItem.setMnemonic(KeyEvent.VK_P);
		preferencesMenuItem.setToolTipText("Set application preferences");
		preferencesMenuItem.addActionListener((ActionEvent event) -> {
			//TODO: Implement Preferences
			System.out.println("Preferences Pressed.");
		});
		
		JMenuItem exitMenuItem = new JMenuItem("Exit");
		exitMenuItem.setMnemonic(KeyEvent.VK_E);
		exitMenuItem.setToolTipText("Exit application");
		exitMenuItem.addActionListener((ActionEvent event) -> {
			System.exit(0);
		});
		
		file.add(preferencesMenuItem);
		file.add(exitMenuItem);
		
		menubar.add(file);
		
		frame.setJMenuBar(menubar);
	}
}
