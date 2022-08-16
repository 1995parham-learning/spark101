package donbal;

import java.math.BigInteger;
import java.time.Instant;

import scala.Tuple2;

public class WordCount {
  private String value;
  private BigInteger count;

  private Tuple2<Instant, Instant> window;

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

  public Tuple2<Instant, Instant> getWindow() {
    return window;
  }

  public void setWindow(Tuple2<Instant, Instant> window) {
    this.window = window;
  }

}
