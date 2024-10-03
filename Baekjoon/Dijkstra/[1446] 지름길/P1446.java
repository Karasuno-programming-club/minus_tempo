package baekjoon.dijkstra;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1446 {
    
    // 간선
    static class Edge {

        // from이 없는 이유는 배열의 위치를 사용하기 때문
        public int to;
        // 가중치
        public int weight;

        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static class Info {
        
        public int idx;
        public int dist;
        
        public Info() {}
        public Info(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }
    }


    /**
     * N: 지름길 개수
     * D: 고속도로 개수
     * length: 길이
     * */ 
    private static int N, D;
    private static int[] dist;
    private static ArrayList<Edge>[] edges;

    static void input() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        // 고속도로 길이만큼 초기화
        dist = new int[D+1];
        edges = new ArrayList[D+1];

        // 고속도로 간 지점 간 기본 이동 구간 설정
        for (int i = 0; i <= D; i++) {
            edges[i] = new ArrayList<>();
            if (i < D) {
                edges[i].add(new Edge(i + 1, 1)); // 1km 이동 간선 추가
            }
        }


        for (int i=0;i<N;i++) {            
            StringTokenizer ist = new StringTokenizer(br.readLine());
            
            int from = Integer.parseInt(ist.nextToken());
            int to = Integer.parseInt(ist.nextToken());
            int weight = Integer.parseInt(ist.nextToken());

            // edges[from].add(new Edge(to, weight));
            // 유효한 지름길만 추가
            if (to <= D && to > from) {
                edges[from].add(new Edge(to, weight));
            }
        }

    }

    static void dijkstra(int start) {
        for (int i = 0; i <= D; i++) dist[i] = Integer.MAX_VALUE;

        PriorityQueue<Info> pq = new PriorityQueue<>((o1, o2) -> o1.dist - o2.dist);


        pq.add(new Info(start,0));
        dist[start] = 0;
        
        while(!pq.isEmpty()) {
            Info info = pq.poll();

            if (dist[info.idx] < info.dist) continue;

            for (Edge e : edges[info.idx]) {
                if(dist[info.idx] + e.weight >= dist[e.to]) continue;

                dist[e.to] = dist[info.idx] + e.weight;
                pq.add(new Info(e.to, dist[e.to]));
            }
        }

        
    }

    public static void main(String[] args) throws Exception{
        input();
        dijkstra(0);
        System.out.println(dist[D]);
    }



}

// 크카카카카어ㅏ롱나ㅓ로ㅓ만이뢈ㄴ얼