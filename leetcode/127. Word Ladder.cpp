#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
#include <queue>
using namespace std;
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string>wordSet(wordList.begin(),wordList.end());
        if(!wordSet.count(endWord))return 0;
        unordered_map<string,int>pathCnt{{{beginWord,1}}};
        queue<string>q{{beginWord}};
        while(!q.empty()){
            string word = q.front();q.pop();
            for (int i =0;i<word.size();++i){
                string newWord = word;
                for(char ch ='a';ch<='z';++ch){
                    newWord[i]=ch;
                    if(wordSet.count(newWord)&&newWord==endWord)return pathCnt[word]+1;
                    if(wordSet.count(newWord)&&!pathCnt.count(newWord)){
                        q.push(newWord);
                        pathCnt[newWord]=pathCnt[word]+1;
                    }
                }
            }
        }
        return 0;
    }
};

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return 0;
        queue<string> q{{beginWord}};
        int res = 0;
        while (!q.empty()) {
            for (int k = q.size(); k > 0; --k) {
                string word = q.front(); q.pop();
                if (word == endWord) return res + 1;
                for (int i = 0; i < word.size(); ++i) {
                    string newWord = word;
                    for (char ch = 'a'; ch <= 'z'; ++ch) {
                        newWord[i] = ch;
                        if (wordSet.count(newWord) && newWord != word) {
                            q.push(newWord);
                            wordSet.erase(newWord);
                        }   
                    }
                }
            }
            ++res;
        }
        return 0;
    }
};