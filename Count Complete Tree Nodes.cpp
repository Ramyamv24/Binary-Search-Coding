#include <iostream>
#include <queue>
#include <cmath>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) {
        val = x;
        left = nullptr;
        right = nullptr;
    }
};

class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr)
            return 0;

        int hl = 0, hr = 0;
        TreeNode *l = root, *r = root;

        while (l) {
            hl++;
            l = l->left;
        }

        while (r) {
            hr++;
            r = r->right;
        }

        if (hl == hr)
            return pow(2, hl) - 1;

        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};

TreeNode* buildTree() {
    int val;
    cout << "Enter root value (-1 for NULL): ";
    cin >> val;

    if (val == -1)
        return nullptr;

    TreeNode* root = new TreeNode(val);
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();

        int leftVal, rightVal;

        cout << "Enter left child of " << curr->val << " (-1 for NULL): ";
        cin >> leftVal;

        if (leftVal != -1) {
            curr->left = new TreeNode(leftVal);
            q.push(curr->left);
        }

        cout << "Enter right child of " << curr->val << " (-1 for NULL): ";
        cin >> rightVal;

        if (rightVal != -1) {
            curr->right = new TreeNode(rightVal);
            q.push(curr->right);
        }
    }

    return root;
}

int main() {
    TreeNode* root = buildTree();

    Solution sol;
    cout << "Number of nodes: " << sol.countNodes(root) << endl;

    return 0;
}