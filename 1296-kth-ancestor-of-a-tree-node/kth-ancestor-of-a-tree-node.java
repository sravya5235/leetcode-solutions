class TreeAncestor {
        /*
        #########################################################################
        #                                                                       #
        #  =============================================                        #
        #                  SIDDARDHA CHILUVERU                                  #
        #  =============================================                        #
        #                                                                       #
        #  Author      : Siddardha Chiluveru                                    #
        #  Description : Solution / Code / Project                              #
        #  Date        : 2026-06-13                                             #
        #                                                                       #
        #########################################################################
        */
        int cols;
        int[][] up;

    public TreeAncestor(int n, int[] parent) {
        String s = Integer.toBinaryString(n);
        cols =0 ;
        for (int i = 0; i < s.length(); i++)
            if (s.charAt(i) == '1') {
                cols = s.length() - i;
                break;
            }
                
        up = new int[n][cols];
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < cols; j++)
                up[i][j] = -1;

        for (int i = 0; i < n; i++)
            up[i][0] = parent[i];

        for (int j = 1; j < cols; j++)
            for (int i = 0; i < n; i++) {
                int k = up[i][j - 1];
                if (k != -1)
                    up[i][j] = up[k][j - 1];
            }
    }
    
    public int getKthAncestor(int node, int k) {
        String s = Integer.toBinaryString(k);
        int len = s.length() - 1;
        for (int i = len; i >= 0; i--) {
            if (s.charAt(i) == '0')
                continue;
            node = up[node][len - i];
            if (node == -1)
                return -1;
        }
        return node;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.getKthAncestor(node,k);
 */