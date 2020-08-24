package si.lj.uni.fmf.pmat.pro2.izpitizpit;



public abstract class Drink implements Printable{
	
	public double volume;
	
	public double alcohol;
	
	public Drink(double volume, double alcohol) {
		this.volume = volume;
		this.alcohol = alcohol;
	}
	
	
	public void main(String[] args) {
		Drink beer = new Beer(volume,alcohol);
		beer.print();
		Drink juice = new Juice(volume,alcohol);
		juice.print();
	}


}


class Beer extends Drink implements Printable{
	
	public Beer(double volume) {
		this(volume, 5);
	}
	
	public Beer(double volume, double alcohol) {
		super(volume, alcohol);
		
		this.volume = volume;
		this.alcohol = alcohol;
	}

	@Override
	public void print() {
		System.out.println(toString());
		
	}
	
}

class Juice extends Drink implements Printable{
	
	public Juice(double volume) {
		this(volume, 0);
	}
	
	public Juice(double volume, double alcohol) {
		super(volume, alcohol);
		
		this.volume = volume;
		this.alcohol = alcohol;
	}

	@Override
	public void print() {
		System.out.println(toString());
		
	}
	
}

interface Printable {
	
	public void print();
	
	}
