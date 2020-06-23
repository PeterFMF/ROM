import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

// https://github.com/lovre/pro2/blob/master/labs/j2/Circles.java

public class Circles extends JFrame {
	
	private static final long serialVersionUID = 1L;
	
	private List<Circle> circles;
	
	public Circles() {
		super();
		
		circles = new ArrayList<Circle>();
		
		setTitle("Circles");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		getRootPane().putClientProperty("apple.awt.brushMetalLook", true);
		setPreferredSize(new Dimension(800, 600));
		setMinimumSize(new Dimension(600, 450));
		setLayout(new BorderLayout());
		
		JPanel console = new JPanel();
		add(console, BorderLayout.NORTH);
		
		JButton delete = new JButton("Delete");
		delete.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				circles.clear();
				repaint();
			}
		});
		console.add(delete);
		
		JButton add = new JButton("Add");
		add.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				circles.add(new Circle(Math.random(), Math.random(), 16));
				repaint();
			}
		});
		console.add(add);
				
		JPanel panel = new JPanel() {
			private static final long serialVersionUID = 1L;
			@Override
			public void paint(Graphics g) {
				super.paint(g);
				for (Circle circle: circles) {
					g.setColor(Color.BLACK);
					
					g.drawOval((int)Math.round(circle.getX() * getWidth()) - circle.getRadius(), (int)Math.round(circle.getY() * getHeight()) - circle.getRadius(), 2 * circle.getRadius(), 2 * circle.getRadius());
				}
			}
		};
		
		panel.setBackground(Color.WHITE);
		add(panel, BorderLayout.CENTER);
	}

	public static void main(String[] args) {
		new Circles().setVisible(true);
	}

}

class Circle {
	
	private double x;
	
	private double y;
	
	private int radius;

	public Circle(double x, double y, int radius) {
		super();
		this.x = x;
		this.y = y;
		this.radius = radius;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	public int getRadius() {
		return radius;
	}	
}