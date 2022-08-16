package donbal;

import java.math.BigInteger;

public class WordCount {
  private String value;
  private BigInteger count;
  private String window;

  public String getWindow() {
    return window;
  }

  public void setWindow(String window) {
    this.window = window;
  }

  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }

  public BigInteger getCount() {
    return count;
  }

  public void setCount(BigInteger count) {
    this.count = count;
  }

}
