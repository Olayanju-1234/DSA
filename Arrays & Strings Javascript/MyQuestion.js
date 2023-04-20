function uniqueEmails(emails) {
  let uniqueEmails = new Set();
  for (let email of emails) {
    let [local, domain] = email.split("@");
    local = local.replace(/\./g, "");
    local = local.split("+")[0];
    uniqueEmails.add(local + "@" + domain);
  };
  return uniqueEmails.size;
}

console.log(uniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]));

function longestPalindromicSubsequence(s) {
  let dp = new Array(s.length).fill(0).map(() => new Array(s.length).fill(0));
//   console.log(dp);
  for (let i = s.length - 1; i >= 0; i--) {
    dp[i][i] = 1;
    for (let j = i + 1; j < s.length; j++) {
      if (s[i] === s[j]) {
        dp[i][j] = dp[i + 1][j - 1] + 2;
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[0][s.length - 1];
}

console.log(longestPalindromicSubsequence("bbbab"));
