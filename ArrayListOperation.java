
class Geeks
{
	public static void insert(ArrayList <Character> clist,char a) {
	    clist.add(a);
	}
	public static void freq(ArrayList <Character> clist,char a){
	    if(clist.contains(a))
	    System.out.println(Collections.freqency(clist,a));
	    else
	    System.out.println("Not Present");
	}
}
