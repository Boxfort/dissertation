package COMNIA;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;

public class SwingGUI
{
	final int WIDTH = 800;
	final int HEIGHT = 600;
	
	private	JFrame frameMainGrid;
	
	public SwingGUI()
	{
		initGUI();
	}
	
	private void initGUI()
	{
		// Main JFrame
		frameMainGrid = new JFrame("COMNIA");
		frameMainGrid.setSize(800, 600);
		frameMainGrid.setLayout(new GridLayout(1,2));
		frameMainGrid.setVisible(true);
		
		// Left Sidebar
		JPanel frameSidebar = new JPanel();
		frameSidebar.setLayout(new CardLayout());
		frameMainGrid.add(frameSidebar);
		
		// Test Button
		JButton testButton = new JButton();
		testButton.setBounds(frameMainGrid.getWidth()/2 - 50,frameMainGrid.getHeight()/2 - 20, 100,40);
		frameMainGrid.add(testButton);
		
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
		
		JMenuItem eMenuItem = new JMenuItem("Exit");
		eMenuItem.setMnemonic(KeyEvent.VK_E);
		eMenuItem.setToolTipText("Exit application");
		eMenuItem.addActionListener((ActionEvent event) -> {
			System.exit(0);
		});
		
		file.add(eMenuItem);
		
		menubar.add(file);
		
		frameMainGrid.setJMenuBar(menubar);
	}
}
