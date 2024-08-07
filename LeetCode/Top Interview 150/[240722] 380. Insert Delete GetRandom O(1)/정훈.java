class RandomizedSet {
    private ArrayList<Integer> list;
    private Map<Integer,Integer> map;

    public RandomizedSet() {
        list = new ArrayList<>();
        map = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val))
            return false;
        list.add(val);
        map.put(val,list.size() - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val))
            return false;
        list.set(map.get(val), list.get(list.size()-1));
        map.put(list.get(map.get(val)), map.get(val));
        list.remove(list.size()-1);
        map.remove(val);
        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()));
    }
}
